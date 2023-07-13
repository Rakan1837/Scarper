import os
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
    os.environ['PATH'] += path   # Change this to path later
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.instacart.ca/store")
    driver.implicitly_wait(25) # waits untill i put in number and give code
    search_input = driver.find_element(By.ID, "search-bar-input")
    # Checkpoint: currently ran into an issue where instacart does not let bot browser through
    # shops unless they're logged in, the above code inputs email and password into the fields, (tested & works)

    # search_input.send_keys(query)
    # sign_in_button = driver.find_element(By.CLASS_NAME, "e-heh46s")
    # sign_in_button.click()
    # action = ActionChains(driver)
    # action.send_keys(Keys.RETURN)
    # action.perform()
    print("tests passed")  
    #driver.quit()
# Example Call Below, will move this to main when details are finalized
path = r"/Users/maleksibai/Desktop/Selenium Driver" 
IC_Scraper("Walmart", path)
