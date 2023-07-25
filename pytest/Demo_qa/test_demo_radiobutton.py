# automating radiobutton
# Importing modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# launching browser and website
def test_radio_button():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demoqa.com/radio-button")

    # inspecting radio button
    radio_button = driver.find_element(By.CLASS_NAME, "custom-control-label")
    radio_button.click()
    time.sleep(5)
   