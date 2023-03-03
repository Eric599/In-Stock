from bs4 import BeautifulSoup
import requests

#URL = "https://www.canakit.com/raspberry-pi-4-starter-kit.html"
URL = "https://www.canakit.com/raspberry-pi-4-extreme-aluminum-case-kit.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="MainContent_PricingDiv")

in_stock = results.findAll("div", class_="add-to-cart")

if len(in_stock) > 0:
    for stock in in_stock:
        print(stock)

#print(soup.prettify)
#print(results.prettify)


# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )