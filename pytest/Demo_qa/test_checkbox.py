# automating check box
# Importing modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# launching browser and open demo qa check box form
# driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
def test_demo():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    time.sleep(3)

    Add = driver.find_element(By.CSS_SELECTOR,
                              "#tree-node > div > button.rct-option.rct-option-expand-all > svg")
    Add.click()
    time.sleep(5)

    Home_checkbox = driver.find_element(By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > label "
                                                         "> span.rct-checkbox > svg")
    Home_checkbox.click()
    time.sleep(5)

    document_react = driver.find_element(By.CSS_SELECTOR,
                                         "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1) > ol > "
                                         "li:nth-child(1) > span > label > span.rct-checkbox > svg")
    document_react.click()
    time.sleep(3)

    office_all_element = driver.find_element(By.CSS_SELECTOR,
                                             "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) "
                                             "> span > label > span.rct-checkbox > svg")
    office_all_element.click()
    time.sleep(3)

    Downloads = driver.find_element(By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > label > "
                                                     "span.rct-checkbox > svg")
    Downloads.click()
    time.sleep(3)
