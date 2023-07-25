# Import required libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdrivermanager import ChromeDriverManager

# Set up the webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager.install(self))

# Navigate to the login page
driver.get("https://www.saucedemo.com/")

# Find the username and password input fields
username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")

# Enter the login credentials
username.send_keys("<your-username>")
password.send_keys("<your-password>")

# Submit the login form
password.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(3)

# Verify that the login was successful by checking for the "Inventory" header
assert "Inventory" in driver.page_source

# Find the first product on the page
product = driver.find_element(By.CSS_SELECTOR,"[class='inventory_item']")

# Get the name and price of the product
product_name = product.find_element(By.CSS_SELECTOR,"[class='inventory_item_name']").text
product_price = float(product.find_element(By.CSS_SELECTOR,"[class='pricebar']").text[1:])

# Add the product to the cart
add_to_cart_button = product.find_element(By.CSS_SELECTOR,"[class='btn_primary btn_inventory']")
add_to_cart_button.click()

# Wait for the page to update
time.sleep(3)

# Verify that the product was added to the cart by checking for the "1" in the shopping cart icon
cart_icon = driver.find_element(By.CSS_SELECTOR,"[class='fa-layers-counter shopping_cart_badge']")
assert "1" in cart_icon.text

# Go back to the product page
driver.back()

# Find the product again
product = driver.find_element(By.CSS_SELECTOR,"[class='inventory_item']")

# Click the product to view its details
product.click()

# Wait for the page to load
time.sleep(3)

# Verify that the product details page has the correct product name, price, and image
assert product_name == driver.find_element(By.CSS_SELECTOR,"[class='inventory_item_name']").text
assert product_price == float(driver.find_element(By.CSS_SELECTOR,"[class='inventory_item_price']").text[1:])
assert "https://" in driver.find_element(By.CSS_SELECTOR,"[class='inventory_item_img")
