from __future__ import annotations

import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

BUY_PRICE = 120
URL = "https://www.amazon.com/dp/B07662ZD8J/ref=twister_B09LN4Q7H4?_encoding=UTF8&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(response.content, "lxml")

price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])
title = soup.find(name="span", id="productTitle").get_text().strip()

load_dotenv()
if price < BUY_PRICE:
    message = f"{title} is now ${price}"
    with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL"),
            to_addrs=os.getenv("EMAIL"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}",
        )
