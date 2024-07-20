import requests
import datetime

APP_ID = "75b1d6dd"
APP_KEY = "98fbab91926b2feff03b5203860bf260"
USERNAME = "nurulhasan"
PASSWORD = "thepasswordforworkoutsheet"

today = datetime.datetime.now()
modified_date = today.strftime("%d/%m/%Y")
modified_time = today.strftime("%X")

exercise_calories_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ab766ad22f28a5f42cdb7bed637e81a9/myWorkouts/workouts"

exercise_calories_parameters = {
    "query": input("which are the exercises you have done today ? "),
    "gender": "male",
    "weight_kg": 89.9,
    "height_cm": 156,
    "age": 19
}

exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=exercise_calories_endpoint, headers=exercise_header, json=exercise_calories_parameters)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": modified_date,
            "time": modified_time,
            "exercise": exercise["name"].title(),
            "duration": f"{exercise['duration_min']}min",
            "calories": exercise["nf_calories"]
        }
    }
    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )

    # Bearer Token Authentication
    # bearer_headers = {
    # "Authorization": f"Bearer {YOUR TOKEN}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=)
    print(sheet_response.text)

