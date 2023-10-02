import requests
from datetime import datetime

#                           NUTRITIONIST

main_endpoint = "https://trackapi.nutritionix.com/v2"

nutrients_url = f"{main_endpoint}/natural/nutrients"

NUTR_APIKEY = "123"
NUTR_ID = "7d"

# user_data = input("What have you eaten today? ")

headers = {
    "x-app-id": NUTR_ID,
    "x-app-key": NUTR_APIKEY
}

parameter = {
    "query": "I have eaten rice and 2 eggs for lunch",
}

food_response = requests.post(url=nutrients_url, json=parameter, headers=headers)

all_food = food_response.json()["foods"]

# item_name = food_response.json()["foods"][:0]["food_name"]
#
# calorie_number = food_response.json()["foods"][0]["nf_calories"]

today = datetime.now()

date_of_event = today.strftime("%d/%m/%Y")

# print(all_food)

# item_name = []
# calorie_number = 0

for item in all_food:
    item_name = item["food_name"]
    calorie_number = item["nf_calories"]

    print(item_name)
    print(calorie_number)


#
# for item in all_food:
#     calorie_number = item["nf_calories"]
#
#     print(calorie_number)


# print(item_name)
# print(calorie_number)
# print(date_of_event)

# print(item_name.text)

#                           GOOGLE SHEETS
sheets_api = "https://api.sheety.co/ed5c031d1b4328c10c2285176f0715cf/calorieCount/sheet1"

# # data_response = requests.get(url=sheets_api)
# # print(data_response.json())
#
# first_row = {
#     "sheet1": {
#         "date": "2/10/23",
#         "name": "rice",
#         "calories": 100
#     }
# }
#
# data_response = requests.post(url=sheets_api, json=first_row)
# print(data_response.text)
