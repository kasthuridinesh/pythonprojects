import time

from swaglabs.pages.base_page import BaseAction
from swaglabs.utils.locator_parser import LocatorConfig


class MenuPage(BaseAction):
    '''Menu button function '''
    MENU_BUTTON = LocatorConfig.get_menu_button()
    ALL_ITEM = LocatorConfig.get_menu_allitem()
    ABOUT = LocatorConfig.get_menu_about()
    RESET_APP = LocatorConfig.get_menu_resetapp()
    ADD_TO_CART = LocatorConfig.get_menu_addcart()
    LOGOUT_BUTTON = LocatorConfig.get_menu_logout()
    CHECK_OUT_BUTTON = LocatorConfig.get_menu_addcart_checkout()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_menubutton(self):
        time.sleep(2)
        self.click_button(self.MENU_BUTTON)
        time.sleep(2)
        return

    def all_menu_button_visible(self):
        ''' Displaying all the details in the menupage'''
        time.sleep(2)
        self.display_details(self.ALL_ITEM)
        self.display_details(self.ABOUT)
        self.display_details(self.LOGOUT_BUTTON)
        self.display_details(self.RESET_APP)
        return

