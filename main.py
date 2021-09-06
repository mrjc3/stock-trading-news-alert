import requests
import os
from notification_manager import NotificationManager


alphavantage_url = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

news_url = "https://newsapi.org/v2/everything"
news_api_key = os.getenv('NEWS_API_KEY')


class StockCheck():
    def __init__(self, symbol):
        self.symbol = symbol

    def percentage_change(self):
        alphavantage_query = {
            "function": "GLOBAL_QUOTE",
            "symbol": self.symbol,
            "apikey": ALPHAVANTAGE_API_KEY
        }

        response = requests.get(alphavantage_url, params=alphavantage_query)
        response.raise_for_status()
        self.stock_data = response.json()
        self.percent_change = self.stock_data['Global Quote']['10. change percent'].strip('').strip("%")
        self.stock = self.stock_data['Global Quote']['01. symbol']
        return float(self.percent_change)

    def get_news(self):
        get_news_query = {
            "apiKey": news_api_key,
            "qInTitle": self.symbol,
            "pageSize": 3,
            "sortBy": "relevancy"
        }

        response = requests.get(news_url, params=get_news_query)
        response.raise_for_status()
        articles = response.json()['articles'][:3]

        self.formatted_articles = [f"{self.symbol}:\n" \
                              f"\nSource: {article['source']['name']}" \
                              f"\nAuthor: {article['author']}" \
                              f"\nTitle: {article['title']}" \
                              f"\nDescription: {article['description']}" \
                              f"\nLink: {article['url']}" for article in articles[:3]]
        return self.formatted_articles


stock = StockCheck('TSLA')
notification = NotificationManager()
message = stock.get_news()


up_down = None
if stock.percentage_change() > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Send the messages if these was a 5% increase or decrease in price of stock
if -5 <= stock.percentage_change() >= 5:
    notification.send_emails(message, up_down)
    notification.send_sms(message, up_down)






