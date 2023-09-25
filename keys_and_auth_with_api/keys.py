import requests
import os
from twilio.rest import Client

account_sid = "AC7c78896325d2a1d6881a6f500a278768"
auth_token = "b70e1fb93d966b30f053cc716ea45aec"


parameters = {
    "lat": 0.347596,
    "lon": 32.582520,
    "appid": "4069afcb8d06a901644c5f8e85209dd3",
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
        from_="+12053080823",
        to="+256700765579"
        )

    print(message.status)
