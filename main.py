# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

sheets = DataManager()
scanner = FlightSearch()
sheet_data = [sheets.read_sheet()]

if sheet_data[0]['prices'][0]["iataCode"] == "":
    for row in sheet_data[0]['prices']:
        row["iataCode"] = scanner.iatacodes(row["city"])
    print(f"sheet_data:\n {sheet_data}")

sheets.data = sheet_data
sheets.update_iata()
