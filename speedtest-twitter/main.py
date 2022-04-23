import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 400
PROMISED_UP = 20


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(os.environ.get("CHROME_DRIVER_PATH")))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Go button
        self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a").click()
        time.sleep(60)

        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                                'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                                'div/div[2]/span').text
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                              'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/'
                                                              'div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/'
                                                    'div/div[1]/label/div/div[2]/div/input') \
            .send_keys(os.environ.get("TWITTER_EMAIL"))

        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/'
                                                    'div/div[2]/label/div/div[2]/div/input') \
            .send_keys(os.environ.get("twitter_password"), Keys.ENTER)

        time.sleep(5)

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"

        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div'
                                                    '[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/'
                                                    'div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')\
            .send_keys(tweet)

        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div'
                                                    '[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/'
                                                    'div[3]').click()

        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    load_dotenv()
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
