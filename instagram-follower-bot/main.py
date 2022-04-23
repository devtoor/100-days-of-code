import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        self.driver.find_element(by=By.NAME, value="username").send_keys(os.environ.get("INSTAGRAM_USERNAME"))
        self.driver.find_element(by=By.NAME, value="password").send_keys(os.environ.get("INSTAGRAM_PASSWORD"),
                                                                         Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{os.environ.get('SIMILAR_ACCOUNT')}")
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
            .click()
        time.sleep(2)

        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            finally:
                time.sleep(1)


if __name__ == '__main__':
    load_dotenv()
    bot = InstaFollower(os.environ.get("CHROME_DRIVER_PATH"))
    bot.login()
    bot.find_followers()
    bot.follow()
