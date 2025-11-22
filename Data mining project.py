
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.101evler.com/kibris/kiralik-emlak/girne?0=&property_type=1&currency=1&property_subtype%5B0%5D=2"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

properties = []

cards = soup.find_all("div", class_="classified")

for card in cards:
    title = card.find("h3").get_text(strip=True) if card.find("h3") else None
    price = card.find("span", class_="price").get_text(strip=True) if card.find("span", class_="price") else None
    location = card.find("div", class_="location").get_text(strip=True) if card.find("div", class_="location") else None
    info = card.find("div", class_="info").get_text(strip=True) if card.find("div", class_="info") else None

    # Image
    img_tag = card.find("img")
    image = img_tag["src"] if img_tag else None

    # Link
    link_tag = card.find("a")
    link = "https://www.101evler.com" + link_tag["href"] if link_tag else None

    properties.append([title, price, location, info, image, link])

df = pd.DataFrame(properties, columns=["Title", "Price", "Location", "Info", "ImageURL", "Link"])
df.to_csv("101evler_girne_rent.csv", index=False)

print("Scraping complete! CSV saved.")
