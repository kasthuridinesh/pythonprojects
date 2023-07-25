import time

from swaglabs.pages.base_page import BaseAction
from swaglabs.utils.locator_parser import LocatorConfig
class LoginPage(BaseAction):
    """Login Page  variables and functions """

    USERNAME_FIELD = LocatorConfig.get_login_user_name()
    PASSWORD_FIELD = LocatorConfig.get_login_password()
    LOGIN_BUTTON = LocatorConfig.get_login_button()
    PAGE_TITLE = LocatorConfig.get_login_pagetitle()
    LOGOUT_BUTTON = LocatorConfig.get_logout_button()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        """login function and passing username and password"""
        time.sleep(2)
        self.send_values(self.USERNAME_FIELD, username)
        self.send_values(self.PASSWORD_FIELD, password)
        time.sleep(2)
        self.click_button(self.LOGIN_BUTTON)
        time.sleep(2)
        return

    def logout(self):
        "logout function"
        time.sleep(2)
        self.click_button(self.LOGOUT_BUTTON)
        time.sleep(2)
        return
