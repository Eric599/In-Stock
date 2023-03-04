from bs4 import BeautifulSoup
import requests

#URL = "https://www.canakit.com/raspberry-pi-4-starter-kit.html"
URL = "https://www.canakit.com/raspberry-pi-4-extreme-aluminum-case-kit.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="MainContent_PricingDiv")

#in_stock = results.findAll("div", id="ProductAddToCartDiv")
stock = results.findAll("div")
models = results.findAll("b")


#print(stock[0].text)
stock_dict = {}

for model in range(len(stock)):
    stock_dict[models[model].text] = stock[model].text
    # print(models[model].text)
    # print(stock[model].text)
    
#print(stock_dict)

for key in stock_dict:
    if stock_dict[key] == "Add to Cart":
        print(key + " is in stock!")