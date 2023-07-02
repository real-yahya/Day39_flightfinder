# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from twilio.rest import Client
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import datetime

sheets = DataManager()
scanner = FlightSearch()
bot = NotificationManager()
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


tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = 'LON'
for destination in sheet_data:
    flight = scanner.flight_search(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight.price < destination['Lowest Price']:
        bot.send_msg(price=flight.price, departure_city=flight.orgin_city, departure_airport=flight.orgin_airport, arrival_city=flight.destination_city,
                     arrival_airport=flight.destination_airport, departure_date=flight.out_date, return_date=flight.return_date)
