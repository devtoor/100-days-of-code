import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

driver = webdriver.Chrome(service=Service(os.environ.get("CHROME_DRIVER_PATH")))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")
item_ids = [
    item.get_attribute("id")
    for item in driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        prices = [
            price.text.split("-")[1].strip().replace(",", "")
            for price in driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
            if price.text
        ]
        cookie_upgrades = {int(prices[n]): item_ids[n] for n in range(len(prices))}
        money = int(
            "".join(
                [
                    char
                    for char in driver.find_element(by=By.ID, value="money").text
                    if char != ","
                ],
            ),
        )
        affordable_upgrades = {
            cost: item_id for cost, item_id in cookie_upgrades.items() if money > cost
        }
        highest_price_affordable_upgrade = max(affordable_upgrades)
        purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(by=By.ID, value=purchase_id).click()
        timeout = time.time() + 5

    if time.time() > five_min:
        print(driver.find_element(by=By.ID, value="cps").text)
        break

driver.quit()
