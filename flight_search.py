import requests
import datetime
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.locApiUrl = "https://api.tequila.kiwi.com/locations/query"
        self.serApiUrl = 'https://api.tequila.kiwi.com/v2/search'
        self.apikey = 'afsKF3L9gQuO1b2kMTDAaNDfPTwdn5Xe'
        self.header = {'apikey': self.apikey}

    def iatacodes(self, city):
        parameters = {
            'term': city,
            'limit': 1
        }
        response = requests.get(
            url=self.locApiUrl, headers=self.header, params=parameters)
        code = response.json()['locations'][0]['code']
        return code

    def flight_search(self, city):
        next_day = datetime.datetime.now() + datetime.timedelta(1)
        six_months = next_day + datetime.timedelta(180)
        parameters = {
            'fly_from': 'LON',
            'fly_to': city,
            'date_from': next_day.strftime("%d/%m/%Y"),
            'date_to': six_months.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            "flight_type": "round",
            'one_per_date': 1,
            "max_stopovers": 0,
            'curr': 'GBP'
        }
        response = requests.get(
            url=self.serApiUrl, headers=self.header, params=parameters)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city}.")
            return None
        print(data)

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
