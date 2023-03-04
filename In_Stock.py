from bs4 import BeautifulSoup
import requests

#URL = "https://www.canakit.com/raspberry-pi-4-starter-kit.html"
URL = "https://www.canakit.com/raspberry-pi-4-extreme-aluminum-case-kit.html"
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
            print(key + " is in stock!")

check_stock()