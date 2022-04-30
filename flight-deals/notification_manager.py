import os
import smtplib

from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.TWILIO_SID = os.getenv("TWILIO_SID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_NUMBER")
        self.TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
        self.EMAIL_PROVIDER_SMTP_ADDRESS = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.EMAIL = os.getenv("EMAIL")
        self.EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.TWILIO_VIRTUAL_NUMBER,
            to=self.TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(self.EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(self.EMAIL, self.EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=self.EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode(
                        "utf-8",
                    ),
                )
