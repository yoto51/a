import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def keep_server_alive():
    driver = webdriver.Chrome()
    driver.get("https://aternos.org/go/")
    time.sleep(5)
    # Add login and button click automation here
    while True:
        time.sleep(600)  # Refresh every 10 minutes
        driver.refresh()

if __name__ == "__main__":
    keep_server_alive()
