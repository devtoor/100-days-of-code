import os

from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.TWILIO_SID = os.environ.get("TWILIO_SID")
        self.TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_NUMBER")
        self.TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.TWILIO_VIRTUAL_NUMBER,
            to=self.TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
