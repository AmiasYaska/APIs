import requests
import datetime as dt

stock_url = "https://www.alphavantage.co/query"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "CH273F3J36IG6BXK"
}

response = requests.get(stock_url, params=parameters_stock)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]

yesterday_close = float(stock_data["2023-09-25"]["4. close"])

today_close = float(stock_data["2023-09-22"]["4. close"])

diff_stock = ((today_close - yesterday_close) / yesterday_close) * 100

print(diff_stock)

if diff_stock > 5 or diff_stock < -5:
    print("Get news")
