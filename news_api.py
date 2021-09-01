import requests

news_url = "https://newsapi.org/v2/everything"
news_api_key = "adb9dc224790479b9170f97f22e1d0e2"

parameters = {
    "apiKey": news_api_key,
    "qInTitle": "TSLA",
    "pageSize": 1,
    "sortBy": "relevancy"
}

response = requests.get(news_url, params=parameters)
response.raise_for_status()
articles = response.json()['articles']
source = articles[0]['source']['name']
author = articles[0]['author']
title = articles[0]['title']
description = articles[0]['description']
link = articles[0]['url']
print(source)
print(author)
print(title)
print(description)
print(link)