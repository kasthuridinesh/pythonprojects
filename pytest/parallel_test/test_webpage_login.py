"""parallel running of all the test scripts. for that , installing xdist module
 for running test parallel :, pytest <filename> - n <num>
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import html


# test the login page of google
def test_google():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()

# test the login page of instagram
def test_instagram():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com/")
    time.sleep(3)
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(3)
    driver.quit()

