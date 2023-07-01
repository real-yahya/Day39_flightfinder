# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

sheets = DataManager()
scanner = FlightSearch()
sheet_data = [sheets.read_sheet()]

sheets.data = sheet_data
sheets.update_iata()
