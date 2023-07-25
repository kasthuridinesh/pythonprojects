# automating table using iframe
# Importing modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_frame_table():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demoqa.com/webtables")
    time.sleep(6)

    Add = driver.find_element(By.ID, "addNewRecordButton")
    Add.click()
    time.sleep(5)

    First_name = driver.find_element(By.ID, "firstName")
    First_name.send_keys("seetha")
    time.sleep(5)

    Second_name = driver.find_element(By.ID, "lastName")
    Second_name.send_keys("rammam")
    time.sleep(6)

    Email = driver.find_element(By.ID, "userEmail")
    Email.send_keys("seetha.ram@gmail.com")
    time.sleep(6)

    Age = driver.find_element(By.ID, "age")
    Age.send_keys(26)
    time.sleep(5)

    Salary = driver.find_element(By.ID, "salary")
    Salary.send_keys("35000")
    time.sleep(5)

    Department = driver.find_element(By.ID, "department")
    Department.send_keys("QA")
    time.sleep(5)

    Submit = driver.find_element(By.ID, "submit")
    Submit.submit()
    time.sleep(6)
