import requests
from twilio.rest import Client

account_sid = "-removed for security-"
auth_token = "-removed for security-"

parameter = {
    "lat": "26.251157321121436",
    "lon": "85.35145249176716",
    "appid": "4c8816a8d8df665e7036529df0b18852",
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
data = response.json()
you_should = False
for num in range(0, 4):
    cords = data["list"][int(num)]["weather"][0]["id"]
    if cords > 600:
        you_should = True

if you_should:
    # print("you should bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='aaee bhya baarish nu hoga, chhata ☔️ le kr jae na..',
        to='whatsapp:+917970569592'
    )
    print(message.status)
# print(data)
