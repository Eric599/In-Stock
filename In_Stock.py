from bs4 import BeautifulSoup
from dotenv import load_dotenv
from twilio.rest import Client
import os
import requests
import logging
import time
import schedule

load_dotenv()
twilio_SID = os.getenv("TwilioSID")
auth = os.getenv("TwilioAuth")
twilio_num = os.getenv("TwilioNum")
my_num = os.getenv("MyNum")
URL = "https://www.canakit.com/raspberry-pi-4-starter-kit.html"
#URL = "https://www.canakit.com/raspberry-pi-4-extreme-aluminum-case-kit.html"
stock_dict = {}

def get_stock(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="MainContent_PricingDiv")
    stock = results.findAll("div")
    models = results.findAll("b")
    for model in range(len(stock)):
        stock_dict[models[model].text] = stock[model].text
    
    
#print(stock_dict)
def check_stock():
    get_stock(URL)
    for key in stock_dict:
        if stock_dict[key] == "Add to Cart":
            client = Client(twilio_SID, auth)
            message = client.messages.create(
                to=my_num, 
                from_=twilio_num,
                body=key + " is in stock!")
            logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.info(message.sid)
            

schedule.every().day.at("08:00").do(check_stock)
schedule.every().day.at("18:00").do(check_stock)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

