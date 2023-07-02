import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.apiURL = "https://api.tequila.kiwi.com/locations/query"
        self.apikey = 'afsKF3L9gQuO1b2kMTDAaNDfPTwdn5Xe'
        self.header = {'apikey': self.apikey}

    def iatacodes(self, city):
        parameters = {
            'term': city,
            'limit': 1
        }
        response = requests.get(
            url=self.apiURL, headers=self.header, params=parameters)
        code = response.json()['locations'][0]['code']
        print(code)
        return code
