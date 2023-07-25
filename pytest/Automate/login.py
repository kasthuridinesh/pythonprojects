import pytest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.run()
def test_Amazon_TC001(input_value):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)
    time.sleep(2)

    # Opening Amazon website and maximizing window
    driver.get('http://www.amazon.in')
    time.sleep(2)
    driver.maximize_window()

    # Mouse hover to sign in button

    signin1 = driver.find_element(By.ID, "nav-link-accountList")
    action.move_to_element(signin1).perform()
    time.sleep(2)
    # Clinking login now button
    login_new = driver.find_element(By.ID, "nav-flyout-ya-signin")
    login_new.click()
    time.sleep(2)

    # Cling create new account button
    create_account = driver.find_element(By.ID, "createAccountSubmit")
    create_account.click()
    time.sleep(2)

    # The name parameter is used to create a new account, and the name is retrieved from the login-data file.
    cust_name = driver.find_element(By.ID, "ap_customer_name")
    cust_name.send_keys(logindata.CUSTOMERNAME)
    time.sleep(2)
    # Passing a mobile number in the number box from the login_data file
    mobile_no = driver.find_element(By.ID, "ap_phone_number")
    mobile_no.send_keys(logindata.MOBILE)
    time.sleep(2)
    # Passing email id from login data
    email_id = driver.find_element(By.ID, "ap_email")
    email_id.send_keys(logindata.MAIL)
    time.sleep(2)
    # Passing password , which is stored in the login-data file
    password = driver.find_element(By.ID, "ap_password")
    password.send_keys(logindata.PASSWOR)
    time.sleep(2)
    # Clicking continue button.
    submit_1 = driver.find_element(By.ID, "continue")
    submit_1.click()
    time.sleep(3)
