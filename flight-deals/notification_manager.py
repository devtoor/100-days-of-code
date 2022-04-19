import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")  # TODO
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")  # TODO
TWILIO_VIRTUAL_NUMBER = "___TWILIO_NUMBER___"  # TODO
TWILIO_VERIFIED_NUMBER = "___YOUR_NUMBER___"  # TODO


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
