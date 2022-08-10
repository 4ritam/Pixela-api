import datetime

import requests

token = "sjdfhshbfhusfwhquhe23r23ir"
username = "pritam4231"

pixela_endpoint = "https://pixe.la"

graph_id = "asjdha112"


# Create New Account
def create_account(token_param: str, username_param: str):
    user_parameter = {
        "token": token_param,
        "username": username_param,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    request = requests.post(url=pixela_endpoint + "/v1/users", json=user_parameter)
    print(request.text)


# Create new graph
def create_graph(title: str, unit: str):
    graph_endpoint = f"{pixela_endpoint}/v1/users/{username}/graphs"
    graph_parameter = {
        "id": "asjdha112",
        "name": title,
        "unit": unit,
        "type": "int",
        "color": "ajisai"
    }
    graph_header = {
        "X-USER-TOKEN": token
    }
    request = requests.post(url=graph_endpoint, json=graph_parameter, headers=graph_header)
    print(request.text)


# Entry in graph
def entry_in_graph(graph: str, quantity: float):
    graph_entry_endpoint = f"{pixela_endpoint}/v1/users/{username}/graphs/{graph}"
    date = str(datetime.date.today()).replace("-", "")
    graph_parameter = {
        "date": date,
        "quantity": str(quantity),

    }
    graph_header = {
        "X-USER-TOKEN": token
    }
    request = requests.post(url=graph_entry_endpoint, json=graph_parameter, headers=graph_header)
    print(request.text)


# create_account(token, username)
# create_graph("Population", "person")

entry_in_graph(graph_id, 5)
