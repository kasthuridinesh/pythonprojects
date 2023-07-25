# **************import modules***************#
import logging
import pytest
from swaglabs.pages import login_page, menu_page
from swaglabs.utils.config_parser import ConfigParserIni


class TestMenu:
    baseURL = ConfigParserIni.get_application_url()
    username = ConfigParserIni.get_username()
    password = ConfigParserIni.get_password()
    logger = logging.getLogger('Test Login')  # Logger

    @pytest.fixture(autouse=True)
    def class_setup1(self, browser_setup):
        self.driver = browser_setup
        self.login = login_page.LoginPage(self.driver)
        self.menu = menu_page.MenuPage(self.driver)

    def test_menu_operation(self):
        self.driver.get(self.baseURL)

        self.login.login(self.username, self.password)

        self.menu.click_menubutton()

        print(self.menu.all_menu_button_visible())  # Exercise 1

        self.login.logout()
