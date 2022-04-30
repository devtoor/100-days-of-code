import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()
driver = webdriver.Chrome(service=Service(os.getenv("CHROME_DRIVER_PATH")))
driver.get("http://www.tinder.com")
sleep(2)

# login button
driver.find_element(
    by=By.XPATH,
    value='//*[@id="content"]/div/div[1]/div/main/div[1]/div'
    "/div/header/div[1]/div[2]/div/button",
).click()
sleep(2)

# FB login
driver.find_element(
    by=By.XPATH,
    value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button',
).click()
sleep(2)

# Switch window to FB window
driver.switch_to.window(driver.window_handles[1])

# Enter FB credentials
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(
    os.getenv("FB_EMAIL"),
)
password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
password.send_keys(os.getenv("FB_PASSWORD"))
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(driver.window_handles[0])
sleep(5)

# Allow location
driver.find_element(
    by=By.XPATH,
    value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]',
).click()
sleep(1)

# Disallow notifications
driver.find_element(
    by=By.XPATH,
    value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]',
).click()
sleep(1)

# Allow cookies
driver.find_element(
    by=By.XPATH,
    value='//*[@id="content"]/div/div[2]/div/div/div[1]/button',
).click()
sleep(1)

for n in range(100):
    sleep(1)
    try:
        # Like button
        driver.find_element(
            by=By.XPATH,
            value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]'
            "/div/div[2]/div[4]/button",
        ).click()
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            driver.find_element(by=By.CSS_SELECTOR, value=".itsAMatch a").click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
