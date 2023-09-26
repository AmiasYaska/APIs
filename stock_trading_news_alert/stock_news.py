import requests
from newsapi import NewsApiClient
import datetime as dt

stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "CH273F3J36IG6BXK"
}

response_stock = requests.get(stock_url, params=parameters_stock)
response_stock.raise_for_status()

stock_data = response_stock.json()["Time Series (Daily)"]

yesterday_close = float(stock_data["2023-09-25"]["4. close"])

today_close = float(stock_data["2023-09-22"]["4. close"])

diff_stock = ((today_close - yesterday_close) / yesterday_close) * 100

print(diff_stock)

if diff_stock > 5 or diff_stock < -5:
    print("Get news")


#                   NEWS


news_params = {
    "q": "ibm",
    "from": "2023-09-25",
    "apiKey": "5bc92d3edf644d36846c615928f45c1b",
}

response_news = requests.get(news_url, params=news_params)
response_news.raise_for_status()

news_data = response_news.json()["articles"]

top_3_news = news_data[:2]
print(top_3_news)
