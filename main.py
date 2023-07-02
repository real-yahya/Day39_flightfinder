# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

sheets = DataManager()
scanner = FlightSearch()
# sheet_data = [sheets.read_sheet()] monthly requests all used
sheet_data = [
    {
        "City": "Paris",
        "IATA Code": "PAR",
        "Lowest Price": 54
    },
    {
        "City": "Berlin",
        "IATA Code": "BER",
        "Lowest Price": 42
    },
    {
        "City": "Tokyo",
        "IATA Code": "TYO",
        "Lowest Price": 485
    },
    {
        "City": "Sydney",
        "IATA Code": "SYD",
        "Lowest Price": 551
    },
    {
        "City": "Istanbul",
        "IATA Code": "IST",
        "Lowest Price": 95
    },
    {
        "City": "Kuala Lumpur",
        "IATA Code": "KUL",
        "Lowest Price": 414
    },
    {
        "City": "New York",
        "IATA Code": "NYC",
        "Lowest Price": 240
    },
    {
        "City": "San Francisco",
        "IATA Code": "SFO",
        "Lowest Price": 260
    },
    {
        "City": "Cape Town",
        "IATA Code": "CPT",
        "Lowest Price": 378
    }

]


# if sheet_data[0]['prices'][0]["iataCode"] == "":
#    for row in sheet_data[0]['prices']:
#        row["iataCode"] = scanner.iatacodes(row["city"])
#    print(f"sheet_data:\n {sheet_data}")
#    sheets.data = sheet_data
#    sheets.update_iata()

for row in sheet_data:
    scanner.flight_search(row['IATA Code'])
