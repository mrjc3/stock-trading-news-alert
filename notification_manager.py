from twilio.rest import Client
import smtplib


TWILIO_SID = "a3084906649044337b74f359f8df481b"
TWILIO_AUTH_TOKEN = "AC9077fa16f8b703c5b8d1f4aaeb5c7dae"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # def send_text(self,):
    #     for article in stock.get_news():
    #         message = client.messages.create(
    #             body=article,
    #             from_='+19282125262',
    #             to='+17194065465',
    #         )


    def send_emails(self, articles):
        my_email = "mrjcthree@gmail.com"
        password = "trashcan123"
        for article in articles:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="mrjc3@outlook.com",
                    msg=article.encode('utf-8')
                )
