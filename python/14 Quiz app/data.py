import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response.json()
question_data = data["results"]
# print(data)
