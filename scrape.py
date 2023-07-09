import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import os
from selenium import webdriver 
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
    os.environ['PATH'] += r"/Users/rakan/Scarper/chromedriver"  # Change this to path later
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.instacart.ca/store")
    # query = "Walmart"
    search_input = driver.find_element(By.ID, "search-bar-input")

    search_input.send_keys(query)

    action = ActionChains(driver)
    action.send_keys(Keys.RETURN)
    action.perform()
    print("tests passed")  
    #driver.quit()
# Example Call Below, will move this to main when details are finalized
path = r"/Users/rakan/Scarper/chromedriver" 
IC_Scraper("Walmart", path)
