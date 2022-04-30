import os
from time import sleep

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(
    url="https://www.zillow.com/homes/San-Francisco,"
    "-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA"
    "%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22"
    "%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22"
    "%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B"
    "%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C"
    "%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22"
    "%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A"
    "%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C"
    "%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header,
)

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.select(".list-card-top a"):
    href = link["href"]
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

addresses = [
    address.get_text().split(" | ")[-1]
    for address in soup.select(".list-card-info address")
]

prices = [price.contents[0] for price in soup.select(".list-card-price")]

driver = webdriver.Chrome(service=Service(os.getenv("CHROME_DRIVER_PATH")))
driver.get("https://forms.gle/9aAMbYttoyP86JMB9")
sleep(3)
for n in range(len(links)):
    sleep(2)

    driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
        "1]/div/div[1]/input",
    ).send_keys(addresses[n])

    driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
        "1]/div/div[1]/input",
    ).send_keys(prices[n])

    driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
        "1]/div/div[1]/input",
    ).send_keys(links[n])

    driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div',
    ).click()
    sleep(2)

    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a",
    ).click()

driver.quit()
