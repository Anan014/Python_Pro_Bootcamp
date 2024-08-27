import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.by import By

load_dotenv("../env/day51_env.env")

PROMISED_DOWN = 600
PROMISED_UP = 300
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
DRIVER_PATH = os.getenv("DRIVER_PATH")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        time.sleep(3)
        accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(45)
        close_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        close_button.click()
        time.sleep(3)

        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        text_to_write = f'Hey Internet provider, why is my internet speed is {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'
        self.driver.get("https://x.com/")
        wait = WebDriverWait(self.driver,20)

        #click x on Welcome
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button'))).click()

        # click Sign in button
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a'))).click()

        # click and enter email
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))).send_keys(TWITTER_EMAIL)

        # click next
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'))).click()

        # click and enter password
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password.send_keys(TWITTER_PASSWORD)

        # press enter
        # password.send_keys(Keys.ENTER)

        # click on Login in button
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))).click()

        # click on X in welcome
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/button'))).click()

        # click on Twitter area and send text
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))).send_keys(text_to_write)

        # click post button
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'))).click()










bot = InternetSpeedTwitterBot(DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
