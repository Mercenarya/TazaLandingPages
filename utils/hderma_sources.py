import requests
import time
import threading
import json
import os,sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(CURRENT, "..")
sys.path.append(ROOT)

from config import url, products_store_xpath, product_name, product_details, product_images

'''
This file is used to define the data structure of the items that we will scrape from the website.
We will use this class to store the data of the items and then convert it to JSON format
'''
class HdermaItem:
    def __init__(self, name,images,prices, link):
        self.name = name
        self.images = images
        # self.details = details
        self.prices = prices
        self.links = link

    def json_result(self):
        return {
            "name": self.name,
            "images": self.images,
            "prices": self.prices,
            # "details": self.details,
            "links": self.links
        }
    
# export item's list and pre-process it to JSON format
def data_sources_generator(url, driver:webdriver.Chrome):
    '''
    This function is used to generate the data sources for the items that we will scrape from the website.
    We will use this function to store the data of the items and then convert it to JSON format
    '''
    try:
        data_queue = []
        driver.get(url)
        
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, products_store_xpath))
        )

        # lấy danh sách 
        item_list = driver.find_elements(By.XPATH, products_store_xpath)
        for item in item_list:
            name = item.find_element(By.XPATH, product_name).text
            # details = item.find_element(By.XPATH, product_details).text
            img_source = item.find_element(By.XPATH,product_images)
            images = [img_source.get_attribute("src") for img in item.find_elements(By.XPATH, product_images)]
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            prices = [price.text for price in item.find_elements(By.CLASS_NAME, 'price')]

            data_queue.append(HdermaItem(name, images, prices, link).json_result())

        return data_queue


    except Exception as e:
        return {
            "error": str(e)
        }



def data_divider(data_queue):
    try:
        name = [x for x in data_queue if x.get("name") or "None"]
        # details = [x for x in data_queue if x.get("details") or "None"]
        image_storage = []

        images = [
            x for x in data_queue if x.get("images") or "None"

        ]
        
        for itm in images:
            if isinstance(itm.get("images"), list):
                image_storage.append(itm.get("images")[0])
           
        links = [x for x in data_queue if x.get("links") or "None" ]
        prices = [x for x in data_queue if x.get("prices") or "None"]
        return {
            "name": name,
            # "details": details,
            "images": image_storage,
            "links": links,
            "prices": prices
        }
    except Exception as e:
        return {
            "error": str(e)
        }



def reveal_data(data_queue):
    '''
    This function is used to reveal the data of the items that we have scraped from the website.
    We will use this function to print the data of the items in JSON format
    '''
    for item in data_queue:
        print(json.dumps(item, indent=4, ensure_ascii=False))


# 
if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    result = data_sources_generator(url, driver)
    # reveal_data(result)
    # print(result)
    print(data_divider(result))
