from __future__ import annotations

import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

parameter = {
    "lat": float(os.getenv("LATITUDE")),
    "lon": float(os.getenv("LONGITUDE")),
    "exclude": "current,minutely,daily",
    "appid": WEATHER_API_KEY,
}
response = requests.get(url=WEATHER_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()["hourly"][:12]

for hour_data in data:
    if hour_data["weather"][0]["id"] < 700:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_=TWILIO_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
        break
