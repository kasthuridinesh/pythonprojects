import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('__incognito')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.maximize_window()

    # # fish automation
    # driver.find_element(By.ID ,"SidebarContent").click()
    # time.sleep(6)


test_browser()
