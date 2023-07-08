from scrape import scrape_instacart
from data_handling import process_data, store_data
from utilities import initialize_webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
This file will be the main file used to run the scraper this main file will contain one function only 
which will call all the other functions by importing them from other files
"""
def main():
    # Specify the store or location to scrape
    search_term = 'Your Store Name'  # Replace with the desired store or location

    # Initialize the WebDriver
    driver = initialize_webdriver()

    # Scrape Instacart
    items_data = scrape_instacart(driver, search_term)

    # Process and store the scraped data
    processed_data = process_data(items_data)
    store_data(processed_data)

    # Close the WebDriver
    driver.quit()

# Entry point of the script
if __name__ == '__main__':
    main()

