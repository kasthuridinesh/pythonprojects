# program using text box
# importing modules
import by as BY

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# launching browser
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


def test_text_box():
    # opening browser
    time.sleep(7)
    driver.get("https://demoqa.com/text-box")

    Name = driver.find_element(By.ID, "userName")
    Name.send_keys("Kasthuri")
    time.sleep(3)

    Email_id = driver.find_element(By.ID, "userEmail")
    Email_id.send_keys("Kasthuri.kandhavel@gmail.com")
    time.sleep(5)

    Current_Address = driver.find_element(By.ID, "currentAddress")
    Current_Address.send_keys("25, Income tax colony,Saravanam patti,Coimbatore")
    time.sleep(5)

    Permanent_address = driver.find_element(By.ID, "permanentAddress")
    Permanent_address.send_keys("karukamani kalam, karukamani , panayur(po), Athicode, Palakkad")
    time.sleep(5)

    Submit = driver.find_element(By.ID, "submit")
    Submit.submit()
    time.sleep(5)
