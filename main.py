from alphavantage_api import StockCheck
from twilio.rest import Client



stock = StockCheck('TSLA')

# change to 5% before submitting final code
if -.05 <= stock.percentage_change() >= .05 :
    print("Get News")

