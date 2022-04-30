from __future__ import annotations

import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
driver = webdriver.Chrome(service=Service(os.getenv("CHROME_DRIVER_PATH")))
driver.get(
    "https://www.linkedin.com/jobs/search?keywords=python%2Bdeveloper&location=Troy%2C%2BNew%2BYork%2C%2BUnited"
    "%2BStates&geoId=103000818&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=2949978366&position=7"
    "&pageNum=0",
)

driver.find_element(by=By.LINK_TEXT, value="Sign in").click()
time.sleep(5)

email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(os.getenv("ACCOUNT_EMAIL"))
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(os.getenv("ACCOUNT_PASSWORD"))
password_field.send_keys(Keys.ENTER)
time.sleep(5)

all_listings = driver.find_elements(
    by=By.CSS_SELECTOR,
    value=".job-card-container--clickable",
)

for listing in all_listings:
    listing.click()
    time.sleep(2)

    try:
        driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button").click()
        time.sleep(5)

        phone = driver.find_element(
            by=By.CLASS_NAME,
            value="fb-single-line-text__input",
        )
        if phone.text == "":
            phone.send_keys(os.getenv("PHONE"))

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            driver.find_element(
                by=By.CLASS_NAME,
                value="artdeco-modal__dismiss",
            ).click()
            time.sleep(2)
            driver.find_elements(
                by=By.CLASS_NAME,
                value="artdeco-modal__confirm-dialog-btn",
            )[1].click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
        time.sleep(2)

        driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
