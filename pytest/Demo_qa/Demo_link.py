# Automating using link


from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# lauching chrome browser and opening website
def test_link():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demoqa.com/links")
    driver.maximize_window()

    Link_Home = driver.find_element(By.ID, "simpleLink")
    Link_Home.click()
    time.sleep(5)

    Link_home2 = driver.find_element(By.ID, "dynamicLink")
    Link_home2.click()
    time.sleep(5)

    Created = driver.find_element(By.ID, "created")
    Created.click()
    time.sleep(5)

    No_content = driver.find_element(By.ID, "no-content")
    No_content.click()
    time.sleep(5)

    Moved = driver.find_element(By.ID, "moved")
    Moved.click()
    time.sleep(5)

    bad_request = driver.find_element(By.ID, "bad-request")
    bad_request.click()
    time.sleep(5)
