import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

# Set window size to simulate mobile view
driver.set_window_size(375, 812)
driver.execute_script("console.log('Mobile view')")
time.sleep(5)

# Set window size to simulate tablet view
driver.set_window_size(768, 1024)
driver.execute_script("console.log('Tablet view')")
time.sleep(5)

# Set window size to simulate desktop view
driver.set_window_size(1280, 800)
driver.execute_script("console.log('Desktop view')")
time.sleep(5)
driver.quit()
