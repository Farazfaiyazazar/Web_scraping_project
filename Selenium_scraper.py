from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Base URL
base_url = "https://www.101evler.com/kibris/kiralik-emlak/girne?0=&property_type=1&currency=1&property_subtype%5B0%5D=2&page={}"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data = []

# Scrape first 3 pages which have 30 items
for page in range(1, 4):
    url = base_url.format(page)
    print(f"Scraping page {page}...")
    driver.get(url)
    time.sleep(10)  # wait for JS content to load

    cards = driver.find_elements(By.CSS_SELECTOR, "div.ilanitembasic")
    print("Found cards:", len(cards))

    for card in cards:
        try:
            price = card.find_element(By.CSS_SELECTOR, ".basicprice").text
        except:
            price = None

        try:
            size = card.find_elements(By.CSS_SELECTOR, ".text-block-130")[0].text
        except:
            size = None

        try:
            type_ = card.find_elements(By.CSS_SELECTOR, ".text-block-130")[1].text
        except:
            type_ = None

        try:
            location = card.find_element(By.CSS_SELECTOR, ".ilanListe131").text
        except:
            location = None

        data.append({
            "price": price,
            "type": type_,
            "size": size,
            "location": location
        })

driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("properties_girne_pages1-3.csv", index=False, encoding="utf-8-sig")

print("Scraping finished! Saved to properties_girne_pages1-3.csv")
