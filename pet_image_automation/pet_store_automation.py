import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('__incognito')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    # driver.get("https://petstore.octoperf.com/actions/Account.action?signonForm=")
    # driver.find_element(By.ID , "stripes--850539762").send_keys("kasthuri")
    # driver.find_element(By.NAME,"password").send_keys("123")
    driver.maximize_window()
    time.sleep(6)

    # driver.find_element(By.XPATH ,"//a[@href='/actions/Catalog.action?viewCategory=&categoryId=FISH']").click()


browser()
