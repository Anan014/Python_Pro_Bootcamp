from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv("../env/day49_env.env")

ACCOUNT_EMAIL = os.getenv("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
PHONE = os.getenv("PHONE")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)


wait = WebDriverWait(driver,20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis"))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(ACCOUNT_EMAIL)
wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(ACCOUNT_PASSWORD)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
driver.get(URL)

sleep(5)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".jobs-search-results__list-item")))
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".jobs-search-results__list-item")

for listing in all_listings:
    # click on a listing job
    wait.until(EC.element_to_be_clickable(listing)).click()

    # click easy apply
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view"))).click()

    # add phone number and click next
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input"))).clear()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input"))).send_keys(PHONE)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

    # click next on upload resume
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

    # add years of work and click review button
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input"))).send_keys("3")
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

    # click submit application button
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()
