import logging
import pytest
from swaglabs.pages import login_page, product_page, menu_page
from swaglabs.utils.config_parser import ConfigParserIni


class TestProductPage:
    baseURL = ConfigParserIni.get_application_url()
    username = ConfigParserIni.get_username()
    password = ConfigParserIni.get_password()
    homepageURL = ConfigParserIni.get_homepage_url()
    firstname = ConfigParserIni.get_firstname()
    lastname = ConfigParserIni.get_lastname()
    pincode = ConfigParserIni.get_pincode()

    logger = logging.getLogger('Test Login')  # Logger

    @pytest.fixture(autouse=True)
    def class_setup(self, browser_setup):
        self.driver = browser_setup
        self.login = login_page.LoginPage(self.driver)
        self.product = product_page.ProductPage(self.driver)
        self.menu = menu_page.MenuPage(self.driver)

    @pytest.mark.run(order=1)
    def test_home_page_title(self):
        self.logger.info("TestLogin")
        self.logger.info("Starting Home Page Title Test ")
        self.driver.get(self.baseURL)
        if self.driver.title == "Swag Labs":
            assert self.driver.title == "Swag Labs"
            self.logger.info("Home Page Title Test Passed")

    @pytest.mark.run(order=3)
    def test_lowest_product(self):
        self.login.login(self.username, self.password)

        self.product.product_page()

        self.product.checkout_product()

        self.product.customer_biodata(self.firstname, self.lastname, self.pincode)

        self.product.final_button()

    @pytest.mark.run(order=4)
    def test_logout(self):
        self.driver.get(self.homepageURL)

        self.menu.click_menubutton()

        self.login.logout()
