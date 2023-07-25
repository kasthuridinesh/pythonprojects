"""
"project name : AMAZON AUTOMATION"
   "project description: Automating some Amazon functionalities using Python, PyCharm, and the Selenium Framework
      "Features of this script:
                   def_test_create account
                   def_test_login
                   def_test_forgot
                   def_test_search product
                   def_test_sort
                   def_test_product display
                   def_test_buy
                   def_test_address
                   def_test_payment
                  def_test_logout
"""
import pytest
######################################################################################################
#                                    Importing Libraries                                             #
######################################################################################################
from selenium import webdriver
import time

import logindata
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

######################################################################################################
#                                    Creating account in Amazon                                      #
######################################################################################################
# launching Chrome browser
@pytest.fixture(scope="module")
def open_browser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('__incognito')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # option = webdriver.ChromeOptions()
    # option.add_argument("--start-maximized")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get('http://www.amazon.in')
    time.sleep(2)
    driver.maximize_window()
    yield
    driver.quit()


def test_Amazon_TC001(open_browser):
     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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

    # Once clicking continue button it shows account already existing with this data.
    # There is one signin option is available in the right corner of this page, we click that sign in link
    ######################################################################################################
    #                            Login Amazon account with credentials                            #
    ######################################################################################################


# singing to amazon

def test_login_TC002(open_browser):
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
    time.sleep(5)
    # Clinking get otp
    get_otp = driver.find_element(By.ID, "continue")
    get_otp.click()
    time.sleep(30)

    # sending opt and submit
    sendotp = driver.find_element(By.ID, "continue")
    sendotp.click()
    time.sleep(3)
    # Clicking continue button after OTP verification done
    submit1 = driver.find_element(By.CLASS_NAME, "a-button-input")
    submit1.click()
    time.sleep(15)
    ######################################################################################################
    #          Searching product in the Amazon website  - TC003                                          #
    ######################################################################################################


def test_search_product_TC003():
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("mobile")
    time.sleep(5)
