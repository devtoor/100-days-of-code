import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = float(os.getenv("WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))

EXERCISE_APP_ID = os.getenv("EXERCISE_APP_ID")
EXERCISE_API_KEY = os.getenv("EXERCISE_API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_TOKEN = os.getenv("SHEET_TOKEN")

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY,
    "Content-Type": "application/json",
}

exercise_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
exercise_response = requests.post(
    url=EXERCISE_ENDPOINT,
    headers=exercise_headers,
    json=exercise_body,
)
exercise_response.raise_for_status()
exercise_list = exercise_response.json()["exercises"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_list:
    sheet_headers = {"Authorization": f"Bearer {SHEET_TOKEN}"}
    sheet_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        },
    }
    sheet_response = requests.post(
        url=SHEET_ENDPOINT,
        json=sheet_body,
        headers=sheet_headers,
    )
    print(sheet_response.text)
