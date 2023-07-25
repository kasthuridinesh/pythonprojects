# automating table using iframe
# Importing modules
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from Demo_qa.test_text_box import driver


def test_demo_button():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demoqa.com/buttons")
    driver.maximize_window()

    double_click = driver.find_element(By.ID, "doubleClickBtn")
    actions = ActionChains(driver)
    actions.double_click(double_click).perform()
    time.sleep(3)

    Right_click = driver.find_element(By.ID, "rightClickBtn")
    actions = ActionChains(driver)
    actions.context_click(Right_click).perform()
    time.sleep(3)

    click_me = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")
    actions = ActionChains(driver)
    actions.click(click_me).perform()
    time.sleep(3)


