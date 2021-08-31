import requests
import os


alphavantage_url ="https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# alphavantage query
alphavantage_query = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": ALPHAVANTAGE_API_KEY
}

response = requests.get(url=alphavantage_url, params=alphavantage_query)
yesterday_stock_data = response.json()["Time Series (Daily)"]
response.raise_for_status()
print(yesterday_stock_data["2021-08-30"])

