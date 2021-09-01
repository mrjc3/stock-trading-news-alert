import requests
import os

alphavantage_url = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

news_url = "https://newsapi.org/v2/everything"
news_api_key = "adb9dc224790479b9170f97f22e1d0e2"

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
        stock_data = response.json()
        self.percent_change = stock_data['Global Quote']['10. change percent'].strip('').strip("%")
        self.stock = stock_data['Global Quote']['01. symbol']
        return float(self.percent_change)

    def get_news(self):
        get_news_query = {
            "apiKey": news_api_key,
            "qInTitle": self.symbol,
            "pageSize": 5,
            "sortBy": "relevancy"
        }

        response = requests.get(news_url, params=get_news_query)
        response.raise_for_status()
        print(response.json())