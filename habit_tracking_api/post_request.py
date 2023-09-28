import requests
from datetime import datetime

#                           CREATE A USER

pixela_url = "https://pixe.la/v1/users"

TOKEN = "bsidbd"
USERNAME = "don"

GRAPH_ID = "graph1"

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_url, json=parameter)
print(response.text)

#               POST HEADERS eg graph

graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

headers_param = {
    "X-USER-TOKEN": TOKEN
}

response_graph = requests.post(url=graph_url, json=graph_params, headers=headers_param)
print(response_graph.text)


#                   POST PIXEL

pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5",
}

pixel_response = requests.post(url=pixel_url, json=pixel_params, headers=headers_param)
print(pixel_response.text)

#                       UPDATE PIXEL

update_url = f"{pixel_url}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "1.5"
}

update_response = requests.put(url=update_url, json=update_params, headers=headers_param)
print(update_response.text)

#                       DELETE A PIXEL

delete_response = requests.delete(url=update_url, headers=headers_param)
print(delete_response.text)



#                       FORMATTING DATE

today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")        # or strftime("%y%m%d") or any other
print(formatted_today)
