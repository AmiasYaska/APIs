import requests

parameters = {
    "lat": 0.347596,
    "lon": 32.582520,
    "appid": "4069afcb8d06a901644c5f8e85209dd3"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
# print(response.status_code)


#
weather_data = response.json()
print(weather_data)
