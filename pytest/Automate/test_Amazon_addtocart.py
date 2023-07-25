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
import action as action
######################################################################################################
#                                    Importing Libraries                                             #
######################################################################################################
from selenium import webdriver
import time
import logindata
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


######################################################################################################
#                                    Creating account in Amazon                                      #
######################################################################################################
# launching Chrome browser
def test_login_TC001():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)
    time.sleep(2)

    # Opening Amazon website and maximizing window
    driver.get('http://www.amazon.in')
    time.sleep(2)
    driver.maximize_window()
'''

# Mouse hover to sign in button

firstLevelMenu = driver.find_element(By.ID, "nav-link-accountList")
action.move_to_element(firstLevelMenu).perform()
time.sleep(2)
# Clinking login now button
secondLLevelMenu = driver.find_element(By.ID, "nav-flyout-ya-signin")
secondLLevelMenu.click()
time.sleep(2)
# Cling create new account button
ThirdLevelMenu = driver.find_element(By.ID, "createAccountSubmit")
ThirdLevelMenu.click()
time.sleep(2)
# The name parameter is used to create a new account, and the name is retrieved from the login-data file.
login = driver.find_element(By.ID, "ap_customer_name")
login.send_keys(logindata.CUSTOMERNAME)
time.sleep(2)
# Passing a mobile number in the number box from the login_data file
login1 = driver.find_element(By.ID, "ap_phone_number")
login1.send_keys(logindata.MOBILE)
time.sleep(2)
# Passing email id from login data
login2 = driver.find_element(By.ID, "ap_email")
login2.send_keys(logindata.MAIL)
time.sleep(2)
# Passing password , which is stored in the login-data file
login3 = driver.find_element(By.ID, "ap_password")
login3.send_keys(logindata.PASSWOR)
time.sleep(2)
# Clicking continue button.
submit1 = driver.find_element(By.ID, "continue")
submit1.click()
time.sleep(3)
'''
# Once clicking continue button it shows account already existing with this data.
# There is one signin option is available in the right corner of this page, we click that sign in link
'''
# singing to amazon
login4 = driver.find_element(By.CLASS_NAME, "a-link-emphasis")
login4.click()
time.sleep(2)
# login with existing data
login = driver.find_element(By.ID, "ap_email")
login.send_keys(logindata.MOBILENO)
time.sleep(2)
# Clicking  continue button
submit = driver.find_element(By.ID, "continue")
submit.click()
time.sleep(1)

Signin = driver.find_element(By.ID, "signInSubmit")
Signin.click()
time.sleep(15)

# sending opt and submit
sendotp = driver.find_element(By.ID, "continue")
sendotp.click()
time.sleep(20)

submit1 = driver.find_element(By.CLASS_NAME, "a-button-input")
submit1.click()
time.sleep(15)

searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
driver.maximize_window()

searchbox.send_keys("mobile")

time.sleep(5)
searchbox.click()
'''
