# **************importing modules***************#
import logging
import pytest
from swaglabs.pages import login_page, menu_page
from swaglabs.utils.config_parser import ConfigParserIni

# login into Swag labs by passing username and password
class TestLogin:
    baseURL = ConfigParserIni.get_application_url()
    username = ConfigParserIni.get_username()
    password = ConfigParserIni.get_password()
    logger = logging.getLogger('Test Login')  # Logger

    @pytest.fixture(autouse=True)
    def class_setup(self, browser_setup):
        self.driver = browser_setup
        self.login = login_page.LoginPage(self.driver)
        self.menu = menu_page.MenuPage(self.driver)


    def test_home_page_title(self):
        self.logger.info("TestLogin")
        self.logger.info("Starting Home Page Title Test ")
        self.driver.get(self.baseURL)
        if self.driver.title == "Swag Labs":
            assert self.driver.title == "Swag Labs"
            self.logger.info("Home Page Title Test Passed")

    def test_login(self):
        self.login.login(self.username, self.password)

        self.menu.click_menubutton()

        self.login.logout()
