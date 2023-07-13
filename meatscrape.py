import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
from time import sleep
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from colorama import Fore
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
# This file will contain the main functions needed to scrape a website of choice


def IC_Scraper(query, path):
    """
    Takes 2 mandatory argument, which will be the name of the store we want to scrape
    This is hard coded for instacart website for now, could be modified later 
    Second argument is the path of the chromedriver on your device
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    os.environ['PATH'] += path   # Change this to path later
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.instacart.ca/store")
    driver.implicitly_wait(25) # waits untill i put in number and give code
    search_input = driver.find_element(By.ID, "search-bar-input")
    search_input.send_keys(query)
    action = ActionChains(driver)
    action.send_keys(Keys.RETURN)
    action.perform()
    store_button = driver.find_element(By.CLASS_NAME, "e-1q8kqdc")
    store_button.click()
    print("tests passed")  

    wait = WebDriverWait(driver, 10)

    # Click on the "Meat & Seafood" section in the left side department list
    meat_seafood_section = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/ul[2]/li[4]/a/span"))) #copy full XPath 
    meat_seafood_section.click()

    #products = driver.find_element(By.CLASS_NAME, "e-13udsys")

    prod_list = driver.find_elements(By.CLASS_NAME, "e-1b0tqp" )

    for prod in prod_list:
        print(prod.text)
    print("----------------")
    #print(products.text)
    
    #driver.quit()

# Example Call Below, will move this to main when details are finalized
path = r"/Users/yusufmoola/Documents/chromedriver_mac64" 
IC_Scraper("Walmart", path)

