# Automating Demo Qa website

from telnetlib import EC

import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v107 import browser
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# from webdriver_manager.core import driver

# import logindata
# from Sub_Function.RegistrationConfig import *


# driver = None


# @pytest.fixture(scope="module")
# def open_browser():
#     global driver
#     option = webdriver.ChromeOptions()
#     option.add_argument("--start-maximized")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get('http://www.google.in')
#     yield
#     driver.quit()


def test_Registration():
    # driver = open_browser
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.google.in')
    driver.get('https://demoqa.com/automation-practice-form')
    # driver.maximize_window()

    login = driver.find_element(By.ID, "firstName")
    login.send_keys("vignesh")
    time.sleep(2)

    login = driver.find_element(By.ID, "lastName")
    login.send_keys("Balakrishnan")
    time.sleep(2)

    login1 = driver.find_element(By.ID, "userEmail")
    login1.send_keys("vignesh5367@gmail.com")
    time.sleep(5)

    btn = driver.find_element(By.XPATH, '//input[@name = "gender"]')
    driver.execute_script("arguments[1].click();", btn)
    time.sleep(2)

    # radio = driver.find_element(By.ID, "gender-radio-1")
    # radio.click()

    login3 = driver.find_element(By.ID, "userNumber")
    login3.send_keys("1234567891")
    time.sleep(2)

    # login3 = driver.find_element(By.ID, "dateOfBirthInput")
    # login3.click()
    # login3.send_keys("19 Mar 1994")

    # date and time picker not working fine

    # datefiel = driver.find_element(By.ID, 'dateOfBirthInput')
    # ActionChains(driver).move_to_element(datefiel).click().send_keys('19 Mar 1994').perform()
    # # login3.send_keys("19 Mar 1994")
    # time.sleep(2)

    login4 = driver.find_element(By.ID, "subjectsInput")
    login4.send_keys("Maths")
    login4.click()
    time.sleep(2)

    btn1 = driver.find_element(By.XPATH, '//input[@id = "hobbies-checkbox-1"]')
    driver.execute_script("arguments[0].click();", btn1)
    time.sleep(2)

    login3 = driver.find_element(By.ID, "uploadPicture")
    # login3.click()
    login3.send_keys("C://Users//vignesh.balakrishnan//Desktop//Sample.png")
    time.sleep(2)

    login3 = driver.find_element(By.ID, "currentAddress")
    login3.send_keys("17a, pattappan kovil st"
                     "sembulichampalayam,tk"
                     "anthiyur"
                     "erode")
    time.sleep(5)
