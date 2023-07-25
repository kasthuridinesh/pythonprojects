from telnetlib import EC

from openpyxl.worksheet.dimensions import Dimension
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
import datetime
from selenium.webdriver.common.action_chains import ActionChains


# from webdriver_manager.core import driver

# import logindata


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
    driver.maximize_window()

    login = driver.find_element(By.ID, "firstName")
    login.send_keys("vignesh")
    time.sleep(2)

    login = driver.find_element(By.ID, "lastName")
    login.send_keys("Balakrishnan")
    time.sleep(2)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    login1 = driver.find_element(By.ID, "userEmail")
    login1.send_keys("vignesh5367@gmail.com")
    time.sleep(5)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    btn = driver.find_element(By.XPATH, '//input[@name = "gender"]')
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)

    login3 = driver.find_element(By.ID, "userNumber")
    login3.send_keys("1234567891")
    time.sleep(2)

    login8 = driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
    login8.click()
    login8 = driver.find_element(By.CSS_SELECTOR,
                                 "#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > "
                                 "div > div.react-datepicker__month-container > div.react-datepicker__month > "
                                 "div:nth-child(3) > div.react-datepicker__day.react-datepicker__day--015")
    login8.click()
    time.sleep(2)

    firstLevelMenu = driver.find_element(By.ID, "subjectsInput")
    firstLevelMenu.send_keys("Maths")
    firstLevelMenu.send_keys(Keys.ENTER)
    # secondLLevelMenu = driver.find_element(By.CSS_SELECTOR,
    #                                        "#subjectsContainer > div > div.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.subjects-auto-complete__value-container--has-value.css-1hwfws3 > div.css-1rhbuit-multiValue.subjects-auto-complete__multi-value > div.css-12jo7m5.subjects-auto-complete__multi-value__label")
    # secondLLevelMenu.click()
    # time.sleep(2)

    btn1 = driver.find_element(By.XPATH, '//input[@id = "hobbies-checkbox-1"]')
    driver.execute_script("arguments[0].click();", btn1)
    time.sleep(2)

    login3 = driver.find_element(By.ID, "uploadPicture")
    # login3.click()
    login3.send_keys("C:\Users\kasthuri.kandavelu\Downloads.jpg")
    time.sleep(2)

    login3 = driver.find_element(By.ID, "currentAddress")
    login3.send_keys("17a, pattappan kovil st"
                     "sembulichampalayam,tk"
                     "anthiyur"
                     "erode")
    time.sleep(5)

    driver.set_window_size(700, 900)

    time.sleep(4)

    page = driver.find_element(By.TAG_NAME, "html")
    page.send_keys(Keys.END)
    time.sleep(4)

    # driver.find_element(By.XPATH, "//*[@id='state']/div/div[2]/div/svg/path").click()
    # time.sleep(5)
