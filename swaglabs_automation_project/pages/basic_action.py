from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Opening amazon website and maximizing window using chrome driver manager -
class open_browser():

    def test_swaplags(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)
        username = driver.find_element(By.XPATH, "//input[@class='input_error form_input']")
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        time.sleep(5)

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        # if login_button.is_enabled():
        #     print("login button is enable")
        # else:
        #     print("login button is not enabled")
        time.sleep(3)

        menu_bar = driver.find_element(By.ID, "react-burger-menu-btn")
        # menu_bar.is_enabled()
        menu_bar.click()
        time.sleep(5)

        # menubar=driver.find_elements(By.ID,"react-burger-menu-btn")
        # for items in menubar:
        #     print(items.text)
        #
        # allitems = driver.find_element(By.XPATH, "//a[@id='inventory_sidebar_link']")
        # if allitems.is_displayed():
        #     print("displayed")
        #
        # about = driver.find_element(By.ID,"about_sidebar_link")
        # if about.is_displayed():
        #     print("about is dispalyed")
        #
        # logout =driver.find_element(By.ID, "logout_sidebar_link")
        # if logout.is_enabled():
        #     print("Logout is enabled")
        #
        #
        # reset_app_state =driver.find_element(By.ID,"reset_sidebar_link")
        # if reset_app_state.is_enabled():
        #     print("reset is enabled")

        # Verify that the login was successful by checking for the "Inventory" header
        # assert "PRODUCTS" in driver.page_source

        # Find all of the products on the page
        products = driver.find_elements(By.CSS_SELECTOR,"[class='inventory_item']")

        # Initialize a variable to keep track of the lowest price
        lowest_price = float("int")

        # Initialize a variable to keep track of the product with the lowest price
        lowest_price_product = None

        # Loop through the products
        for product in products:
            # Get the price of the product
            price = float(product.find_element(By.CSS_SELECTOR,"[class='pricebar']").text[1:])

            # Check if the price is lower than the current lowest price
            if price < lowest_price:
                lowest_price = price
                lowest_price_product = product

        # Add the product with the lowest price to the cart
        add_to_cart_button = lowest_price_product.find_element(By.CSS_SELECTOR,"[class='btn_primary btn_inventory']")
        add_to_cart_button.click()

        # Wait for the page to update
        time.sleep(3)

        # Verify that the product was added to the cart by checking for the "1" in the shopping cart icon
        cart_icon = driver.find_element(By.CSS_SELECTOR,"[class='fa-layers-counter shopping_cart_badge']")
        assert 1 in cart_icon.text

        # Go to the cart page
        cart_icon.click()

        # Wait for the page to load
        time.sleep(3)

        # Verify that the product in the cart has the correct name and price by checking for the product name and price on the page
        product_name = driver.find_element(By.CSS_SELECTOR,"[class='inventory_item_name']").text
        product_price = float(driver.find_element(By.CSS_SELECTOR,"[class='inventory_item_price']").text[1:])
        print(product_name)
        print(product_price)




obj = open_browser()
obj.test_swaplags()
