import os

import requests

from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        self.TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")
        self.TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
        self.HEADERS = {"apikey": self.TEQUILA_API_KEY}

    def get_destination_code(self, city_names):
        codes = []
        for city in city_names:
            query = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/locations/query", headers=self.HEADERS, params=query)
            codes.append(response.json()["locations"][0]["code"])
        return codes

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 21,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/v2/search", headers=self.HEADERS, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/v2/search", headers=self.HEADERS, params=query)
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}\n"
                  f"From: {flight_data.origin_airport} {flight_data.out_date}, VIA: {flight_data.via_city}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}\n"
                  f"From: {flight_data.origin_airport} {flight_data.out_date}")
            return flight_data
