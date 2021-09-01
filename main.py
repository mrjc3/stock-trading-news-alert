import requests
import os
from twilio.rest import Client


alphavantage_url ="https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

symbols = ["IBM", "TSLA", "MSFT",]


# alphavantage query

for symbol in symbols:
    alphavantage_query = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY
    }

    response = requests.get(alphavantage_url, params=alphavantage_query)
    response.raise_for_status()
    stock_data = response.json()
    percent_change = stock_data['Global Quote']['10. change percent']
    stock = stock_data['Global Quote']['01. symbol']
    print(f'{stock}: {percent_change}')
