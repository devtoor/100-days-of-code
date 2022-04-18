import requests
import os
from datetime import datetime

GENDER = "___YOUR_GENDER___"  # TODO
WEIGHT_KG = "___YOUR_WEIGHT_KG___"  # TODO
HEIGHT_CM = "___YOUR_HEIGHT_CM___"  # TODO
AGE = "___YOUR_AGE___"  # TODO

EXERCISE_APP_ID = os.environ.get("EXERCISE_APP_ID")  # TODO
EXERCISE_API_KEY = os.environ.get("EXERCISE_API_KEY")  # TODO
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")  # TODO
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")  # TODO

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY,
    "Content-Type": "application/json"
}

exercise_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
exercise_response = requests.post(url=EXERCISE_ENDPOINT, headers=exercise_headers, json=exercise_body)
exercise_response.raise_for_status()
exercise_list = exercise_response.json()["exercises"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_list:
    sheet_headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}"
    }
    sheet_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_body, headers=sheet_headers)
    print(sheet_response.text)
