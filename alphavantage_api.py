import requests
import os
from twilio.rest import Client


alphavantage_url = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = "C5N1XKZX63E8KBUX"

news_url = "https://newsapi.org/v2/everything"
# news_api_key = os.getenv('NEWS_API_KEY')
news_api_key = "adb9dc224790479b9170f97f22e1d0e2"

TWILIO_SID = "a3084906649044337b74f359f8df481b"
TWILIO_AUTH_TOKEN = "AC9077fa16f8b703c5b8d1f4aaeb5c7dae"

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

        self.formatted_articles = [f"{self.symbol}: {self.percentage_change()}%" \
                              f"\nSource: {article['source']['name']}" \
                              f"\nAuthor: {article['author']}" \
                              f"\nTitle: {article['title']}" \
                              f"\nDescription: {article['description']}" \
                              f"\nLink: {article['url']}" for article in articles[:3]]
        return self.formatted_articles

    def send_text(self):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for article in stock.get_news():
            message = client.messages.create(
                body=article,
                from_='+19282125262',
                to='+17194065465',
            )


stock = StockCheck("MSFT")
print(stock.percentage_change())
stock.send_text()

#TODO Fix the api key read documentation try x-api key
