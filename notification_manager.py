from twilio.rest import Client
import smtplib
import os

# TWILIO_SID = os.environ['TWILIO_SID']
# TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
MY_TWILIO_NUMBER = os.getenv('MY_TWILIO_NUMBER')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, articles, direction):
        for article in articles:
            message = self.client.messages.create(
                body=f'{direction} {direction} {direction} {article}',
                from_=MY_TWILIO_NUMBER,
                to='+9519016131',
            )
            # Prints if successfully sent.
            print(message.status)

    def send_emails(self, articles, direction):
        my_email = os.getenv('MY_EMAIL')
        password = os.getenv('PASSWORD')
        for article in articles:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs='myemail@outlook.com',
                    msg=f'{direction} {direction} {direction} {article}'
                )
