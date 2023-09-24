import requests

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": "4069afcb8d06a901644c5f8e85209dd3"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)
