import requests
import datetime

USERNAME = "nurulhasan"
TOKEN = "--- generated token ---"
today = datetime.datetime.now()


pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    # token string is actually self created API-key
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "coding",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

record_endpoint = f"{graph_endpoint}/{graph_config['id']}"
formatted_date = today.strftime("%Y%m%d")
record_config = {
    "date": formatted_date,
    "quantity": input("how many hours did you code today ? ")
}

response = requests.post(url=record_endpoint, json=record_config, headers=header)
print(response.text)

put_endpoint = f"{record_endpoint}/{formatted_date}"
record_put = {
    "quantity": "5"
}

# response = requests.put(url=put_endpoint, json=record_put, headers=header)
# print(response.text)
