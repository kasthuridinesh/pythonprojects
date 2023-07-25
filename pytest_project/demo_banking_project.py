import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Opening  website and maximizing window using chrome driver manager
def test_guru_TC001():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demo.guru99.com/")
    driver.maximize_window()
    time.sleep(5)

    # selecting Bank
    bank_project = driver.find_element(By.LINK_TEXT, "Bank Project")
    bank_project.click()
    time.sleep(5)

    # passing credentials(login id and user and  name )
    user_id = driver.find_element(By.XPATH, "//input[@name='uid']")
    user_id.send_keys("mngr472933")
    time.sleep(5)

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("UqEryra")
    time.sleep(5)

    login = driver.find_element(By.XPATH, "//input[@name='btnLogin']")
    login.click()
    time.sleep(5)

    # selecting customer
    new_customer = driver.find_element(By.LINK_TEXT, "New Customer")
    new_customer.click()
    time.sleep(5)

    # Filling customer name
    customer_name = driver.find_element(By.XPATH, "//input[@name ='name']")
    customer_name.send_keys("Kasthuri")
    time.sleep(5)

    # filling address
    address = driver.find_element(By.NAME, "addr")
    address.send_keys("25 Incometax colony")
    time.sleep(5)

    city = driver.find_element(By.XPATH, "//input[@name ='city']")
    city.send_keys("Coimbatore")
    time.sleep(5)

    state = driver.find_element(By.XPATH, "//input[@name ='state']")
    state.send_keys("Tamil nadu")
    time.sleep(5)

    pincode = driver.find_element(By.XPATH, "//input[@name ='pinno']")
    pincode.send_keys("678552")
    time.sleep(5)

    telephone = driver.find_element(By.XPATH, "//input[@name ='telephoneno']")
    telephone.send_keys("7293062280")
    time.sleep(5)

    email_id = driver.find_element(By.XPATH, "//input[@name ='emailid']")
    email_id.send_keys("asdf@gmail.com")
    time.sleep(5)
