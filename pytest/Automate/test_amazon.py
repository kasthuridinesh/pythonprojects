from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Opening amazon website and maximizing window using chrome driver manager -
def test_amazon_TC001():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('__incognito')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(5)

    searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
    driver.maximize_window()
    # parent_window = driver.current_window_handle
    searchbox.send_keys("mobile")

    time.sleep(5)
    searchbox.click()
