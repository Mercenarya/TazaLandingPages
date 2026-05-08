import os,sys
import json
import numpy as np
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.join(CURRENT, "..")
sys.path.append(ROOT)

from config import url
from utils.hderma_sources import data_sources_generator, reveal_data, data_divider
from utils.data_insert import input_data,data, input_data_from_json


if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    result = data_sources_generator(url, driver)
    # reveal_data(result)
    list_result = data_divider(result)
    print("name's size: ", len(list_result.get("name")))
    print("images's size: ", len(list_result.get("images")))
    print("prices's size: ", len(list_result.get("prices")))
    print("links's size: ", len(list_result.get("links")))

    print(input_data_from_json(data, result))