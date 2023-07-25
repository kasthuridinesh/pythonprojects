from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#  launching browser
def test_amazon_login():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.get(
        "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F"
        "%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
        "&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth"
        "%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    # automating search box
    login = driver.find_element(By.ID, "ap_email")
    login.send_keys("kasthuri.kandhavel@gmail.com")
    time.sleep(2)
    # automating continue button
    submit = driver.find_element(By.ID, "continue")
    submit.click()
    time.sleep(5)

    # automate send otp
    driver.find_element(By.ID, "continue").click()
    time.sleep(120)

