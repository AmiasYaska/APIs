import requests

pixela_url = "https://pixe.la/v1/users"

TOKEN = "bsidbdu764hdih"
USERNAME = "donnyvan"

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_url, json=parameter)
# print(response.text)

#               post headers

graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
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
