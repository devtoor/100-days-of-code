from __future__ import annotations

import os
import smtplib
import time
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LATITUDE = float(os.getenv("LATITUDE"))
LONGITUDE = float(os.getenv("LONGITUDE"))


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (
        LATITUDE - 5 <= iss_latitude <= LATITUDE + 5
        and LONGITUDE - 5 <= iss_longitude <= LONGITUDE + 5
    )


def is_night():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }
    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params=parameters,
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SMTP_ADDRESS)
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky.",
        )
