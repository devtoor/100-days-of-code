import os

import requests


class DataManager:
    def __init__(self):
        self.SHEET_FLIGHT_ENDPOINT = os.getenv("SHEET_FLIGHT_ENDPOINT")
        self.SHEET_USERS_ENDPOINT = os.getenv("SHEET_USERS_ENDPOINT")
        self.SHEET_TOKEN = os.getenv("SHEET_TOKEN")
        self.HEADERS = {"Authorization": f"Bearer {self.SHEET_TOKEN}"}

    def get_destination_data(self) -> {}:
        response = requests.get(url=self.SHEET_FLIGHT_ENDPOINT, headers=self.HEADERS)
        return response.json()["prices"]

    def update_destination_codes(self, codes):
        index = 2
        for code in codes:
            body = {"price": {"iataCode": code}}
            response = requests.put(
                url=f"{self.SHEET_FLIGHT_ENDPOINT}/{index}",
                headers=self.HEADERS,
                json=body,
            )
            print(response.text)
            index += 1

    def get_customer_emails(self):
        response = requests.get(self.SHEET_USERS_ENDPOINT, headers=self.HEADERS)
        return response.json()["users"]
