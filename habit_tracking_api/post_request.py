import requests
from datetime import datetime

#                           create a user

pixela_url = "https://pixe.la/v1/users"

TOKEN = "bsidbdu764hdih"
USERNAME = "donnyvan"

GRAPH_ID = "graph1"

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_url, json=parameter)
# print(response.text)

#               post headers eg graph

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

# response_graph = requests.post(url=graph_url, json=graph_params, headers=headers_param)
# print(response_graph.text)


#                   post a pixel

pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5",
}

# pixel_response = requests.post(url=pixel_url, json=pixel_params, headers=headers_param)
# print(pixel_response.text)




#                       FORMATTING DATE
# today = dt.datetime.now()
# formatted_today = today.strftime("%Y-%m-%d")
# print(formatted_today)
