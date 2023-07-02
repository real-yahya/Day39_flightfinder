from twilio.rest import Client



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = 'AC096814d690f5a3310cf563a92b96c6bc'
        self.auth_token = '806e6d7ee8b5eb4c8982d1696a424c0f'

    def send_msg(self,price,departure_city,departure_airport,arrival_city,arrival_airport,departure_date,return_date):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
                body=f"Low price alert! only {price} to fly from {departure_city}-{departure_airport} to {arrival_city}={arrival_airport} from {departure_date} to {return_date}",
                from_='+447429090497',
                to='+447858304559'
            )
        print(message)
    

    #def send_mesage(self):
    #    client = Client(self.account_sid, self.auth_token)
    #    message = client.messages.create(
    #            body="hi , i work",
    #            from_='+447429090497',
    #            to='+447858304559'
    #        )
    #    print(message.sid)


