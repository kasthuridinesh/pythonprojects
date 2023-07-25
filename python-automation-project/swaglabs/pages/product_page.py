import time

from swaglabs.pages.base_page import BaseAction
from swaglabs.utils.locator_parser import LocatorConfig
class ProductPage(BaseAction):
    ''' Inherits functions from basepage '''
    ADD_TO_CART = LocatorConfig.get_product_addcart()
    CHECK_OUT_BUTTON = LocatorConfig.get_product_checkout()
    LOWEST_PRODUCT_ADD = LocatorConfig.get_product_lowest_product_add()
    FIRST_NAME = LocatorConfig.get_product_firstname()
    LAST_NAME = LocatorConfig.get_product_lastname()
    POSTAL_CODE = LocatorConfig.get_product_pincode()
    CUSTOMER_DETAILS_CHECKOUT_BUTTON = LocatorConfig.get_product_customer_checkout()
    FINAL_FINISH_BUTTON = LocatorConfig.get_product_finish_button()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def product_page(self):
        self.scroll_down_funtion()
        self.click_button(self.LOWEST_PRODUCT_ADD)
        time.sleep(2)
        self.scroll_up_funtion()
        self.click_button(self.ADD_TO_CART)
        time.sleep(2)
        return

    def checkout_product(self):
        self.click_button(self.CHECK_OUT_BUTTON)
        time.sleep(2)
        return

    def customer_biodata(self, firstname, lastname, pincode):
        """ passing customer firstname, lastname and pincode"""
        time.sleep(2)
        self.send_values(self.FIRST_NAME, firstname)
        time.sleep(3)
        self.send_values(self.LAST_NAME, lastname)
        time.sleep(3)
        self.send_values(self.POSTAL_CODE, pincode)
        time.sleep(2)
        self.scroll_down_funtion()
        time.sleep(2)
        self.click_button(self.CUSTOMER_DETAILS_CHECKOUT_BUTTON)
        return

    def final_button(self):
        time.sleep(2)
        self.click_button(self.FINAL_FINISH_BUTTON)
        self.scroll_up_funtion()
        return

