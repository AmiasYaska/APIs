import requests

parameters = {
    "lat": 0.347596,
    "lon": 32.582520,
    "appid": "4069afcb8d06a901644c5f8e85209dd3",
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_list = weather_data["list"][0]["weather"][0]["id"]

print(weather_list)

for i in weather_data["list"][:12]:
    weather_id = i["weather"][0]["id"]
    if int(weather_id) < 700:
        print("Carry an umbrella")
