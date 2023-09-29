import requests

#                           NUTRIONIST

main_endpoint = "https://trackapi.nutritionix.com/v2"

nutrients_url = f"{main_endpoint}/natural/nutrients"

NUTR_APIKEY = "111eb5793b5a11f73193522e19eef222"
NUTR_ID = "7d43be49"

user_data = input("What have you eaten today? ")

headers = {
    "x-app-id": NUTR_ID,
    "x-app-key": NUTR_APIKEY
}

parameter = {
    "query": user_data,
}

response = requests.post(url=nutrients_url, json=parameter, headers=headers)
print(response.text)


