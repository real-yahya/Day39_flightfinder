import requests


class DataManager:
    def __init__(self):
        self.apiURL = "https://api.sheety.co/ae6e597461e60d80ebb76f45afe11f2a/flightDeals/prices"
        self.data = {}

    def read_sheet(self):
        response = requests.get(self.apiURL)
        self.data = response.json()
        return self.data

    def update_iata(self):
        for city in self.data[0]["prices"]:
            iata = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{self.apiURL}/{city['id']}", json=iata)
            print(response.text)
