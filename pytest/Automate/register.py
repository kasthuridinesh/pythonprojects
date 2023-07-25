import pytest
from selenium import webdriver
import time
from webdriver_manager.core import driver
import logindata
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.run()
def test_login():
    login_2 = driver.find_element(By.CLASS_NAME, "a-link-emphasis")
    login_2.click()
    time.sleep(2)
    # login with existing data
    mobile_no = driver.find_element(By.ID, "ap_email")
    mobile_no.send_keys(logindata.MOBILENO)
    time.sleep(2)
    # Clicking  continue button
    continue_login = driver.find_element(By.ID, "continue")
    continue_login.click()
    time.sleep(1)

    Signin = driver.find_element(By.ID, "signInSubmit")
    Signin.click()
    time.sleep(1)
    # Clinking get otp
    get_otp = driver.find_element(By.ID, "continue")
    get_otp.click()
    time.sleep(1)

    # sending opt and submit
    sendotp = driver.find_element(By.ID, "continue")
    sendotp.click()
    time.sleep(20)
    # Clicking continue button after OTP verification done
    submit1 = driver.find_element(By.CLASS_NAME, "a-button-input")
    submit1.click()
    time.sleep(15)
