import time

from selenium import webdriver


# launching the browser

def browser():
    driver = webdriver.Chrome()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.maximize_window()
    time.sleep(5)

    # chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_experimental_option('__incoginato')
    # driver = webdriver.Chrome(chrome_options=chrome_option)
    # driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    # driver.maximize_window()
    # #


browser()
