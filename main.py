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
notification.send_emails(message)
# print(stock.percentage_change())


# change to 5% before submitting final code
# if -.05 <= stock.percentage_change() >= .05 :
#     pass

#TODO Fix the api key read documentation try x-api key



