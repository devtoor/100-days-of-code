import requests
import os
from twilio.rest import Client

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")

parameter = {
    "lat": 0.0000001,       #TODO
    "lon": -0.0000001,      #TODO
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
            from_="__TWILIO NUMBER__",  #TODO
            to="__YOUR NUMBER__",       #TODO
        )
        print(message.sid)
        break
