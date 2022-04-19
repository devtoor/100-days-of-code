import requests
import os

SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")  # TODO
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")  # TODO
HEADERS = {"Authorization": f"Bearer {SHEET_TOKEN}"}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self) -> {}:
        response = requests.get(url=SHEET_ENDPOINT, headers=HEADERS)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    @staticmethod
    def update_destination_codes(codes):
        index = 2
        for code in codes:
            body = {
                "price": {
                    "iataCode": code
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{index}", headers=HEADERS, json=body)
            print(response.text)
            index += 1
