import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from swaglabs.pages.base_page import BaseAction
from swaglabs.utils.locator_parser import LocatorConfig


class Product_View(BaseAction):
    """ Inherits functions from basepage and
    Product details functions like name , price and image """
    add_product_button = LocatorConfig.get_product_view_add_button()
    click_product_name = LocatorConfig.get_product_view_click_productname()
    product_detail_page_name = LocatorConfig.get_product_view_click_productname()
    product_detail_page_price = LocatorConfig.get_product_view_price_details()
    product_detail_page_image = LocatorConfig.get_product_view_image_details()
    product_detail_page_remove_button = LocatorConfig.get_product_view_remove_button()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def product_page(self):
        time.sleep(2)
        self.click_button(self.add_product_button)
        time.sleep(2)
        self.click_button(self.click_product_name)
        time.sleep(2)
        self.get_text(self.product_detail_page_name)
        time.sleep(2)
        self.get_text(self.product_detail_page_price)
        time.sleep(2)
        self.get_text(self.product_detail_page_image)
        time.sleep(2)
        self.display_details(self.product_detail_page_remove_button)
        return

