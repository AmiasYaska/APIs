import requests
from twilio.rest import Client


stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

twilio_account_sid = 'ABC'
twilio_auth_token = '[AuthToken]'

stock_apikey = "ABC"
news_apikey = "123"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_apikey
}

response_stock = requests.get(stock_url, params=parameters_stock)
response_stock.raise_for_status()

stock_data = response_stock.json()["Time Series (Daily)"]

stock_list = [value for (key, value) in stock_data.items()]     # converts dict to list ie list comprehension

yesterday_close = float(stock_list[0]["4. close"])

today_close = float(stock_list[1]["4. close"])

diff_stock = (abs(today_close - yesterday_close) / yesterday_close) * 100       # abs gets the magnitude

print(diff_stock)


#                           NEWS

if diff_stock > 1:
    news_params = {
        "q": "Tesla Inc",
        "from": "2023-09-25",
        "apiKey": news_apikey
    }

    response_news = requests.get(news_url, params=news_params)
    response_news.raise_for_status()

    news_data = response_news.json()["articles"]

    top_3_news = news_data[:3]

    formatted_articles = [f"{article['title']}.\n{article['description']}" for article in top_3_news]

    print(formatted_articles)

#                       TWILIO SMS

    client = Client(twilio_account_sid, twilio_auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="123",
            to='567'

        )
