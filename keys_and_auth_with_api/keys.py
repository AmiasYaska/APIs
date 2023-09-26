import requests
import os
from twilio.rest import Client
# from twilio.http.http_Client import TwilioHttpClient

account_sid = "abcd"
auth_token = os.environ.get("AUTH_TOKEN")               # env variable

parameters = {
    "lat": 0.347596,
    "lon": 32.582520,
    "appid": "xyz",
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_list = weather_data["list"][0]["weather"][0]["id"]

# print(weather_list)

will_rain = False

for i in weather_data["list"][:12]:
    weather_id = i["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="You should carry an umbrella ☂️.",
            from_="+120000",
            to="+0000"
        )

    print(message.status)
