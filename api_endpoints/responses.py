import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()             # to capture errors

data = response.json()
lat_position = data["iss_position"]["latitude"]

print(lat_position)
