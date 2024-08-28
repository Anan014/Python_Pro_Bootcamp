import pprint

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
SHEET_URL = "https://forms.gle/WArao4r72J8gC9Xo9"


class GetData:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.all_properties = []


    def get_zillow(self):
        zillow_page = requests.get(ZILLOW_URL, headers=HEADER)

        soup = BeautifulSoup(zillow_page.content, "html.parser")
        results = soup.find("ul", class_="List-c11n-8-84-3-photo-cards")

        properties_elements = results.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        for property in properties_elements:
            link = property.find("a", class_="StyledPropertyCardDataArea-anchor")["href"]

            price_element = property.find("span", class_="PropertyCardWrapper__StyledPriceLine").text
            price = ''
            if "$" in price_element:
                price = price_element.replace("/mo", "").split("+")[0]

            address_element = property.find("address").text
            address = address_element.replace(" | ", " ").strip()

            property_dictionary = {
                "link": link,
                "price": price,
                "address": address
            }
            self.all_properties.append(property_dictionary)
            # pprint.pprint(self.all_properties)

    def get_selenium(self):
        self.driver.get(SHEET_URL)
        time.sleep(5)

        for counter, property_item in enumerate(self.all_properties):
            address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
            address = self.driver.find_element(by=By.XPATH,value=address_xpath)
            address.send_keys(property_item["address"])

            price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
            price = self.driver.find_element(by=By.XPATH,value=price_xpath)
            price.send_keys(property_item["price"])

            link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
            link = self.driver.find_element(by=By.XPATH,value=link_xpath)
            link.send_keys(property_item["link"])

            submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
            submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)
            submit_button.click()
            time.sleep(2)
            print(f"Added: {counter}")

            send_again_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
            send_again_button = self.driver.find_element(by=By.XPATH, value=send_again_button_xpath)
            send_again_button.click()
            time.sleep(2)



bot = GetData()
bot.get_zillow()
bot.get_selenium()

