# **************import modules***************#
import pytest
from swaglabs.pages import login_page, menu_page, product_detail_page
from swaglabs.utils.config_parser import ConfigParserIni
import logging
class TestProduct:
    baseURL = ConfigParserIni.get_application_url()
    username = ConfigParserIni.get_username()
    password = ConfigParserIni.get_password()
    homepage = ConfigParserIni.get_homepage_url()

    logger = logging.getLogger('Test Login')  # Logger

    @pytest.fixture(autouse=True)
    def class_setup(self, browser_setup):
        self.driver = browser_setup
        self.login = login_page.LoginPage(self.driver)
        self.menu = menu_page.MenuPage(self.driver)
        self.product = product_detail_page.Product_View(self.driver)

    @pytest.mark.run(order=1)
    def test_home_page_title(self):
        self.logger.info("TestLogin")
        self.logger.info("Starting Home Page Title Test ")
        self.driver.get(self.baseURL)
        if self.driver.title == "Swag Labs":
            assert self.driver.title == "Swag Labs"
            # self.logger.info("Home Page Title Test Passed")

    def test_login(self):
        self.login.login(self.username, self.password)

        self.product.product_page()

        self.driver.get(self.homepage)

        self.menu.click_menubutton()

        self.login.logout()
