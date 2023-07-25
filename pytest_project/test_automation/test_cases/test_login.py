import pytest
from test_automation.page_objects.login_page import LoginPage
from test_automation.utilities.read_properties import ReadConfig
import time


@pytest.mark.usefixtures('browser_setup')
class TestLogin:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    customername = ReadConfig.get_customername()
    dateofbirth = ReadConfig.get_dateofbirth()

    @pytest.fixture(autouse=True)
    def class_setup(self, browser_setup):
        self.driver = browser_setup

    @pytest.mark.sanity
    def test_home_page_title(self):
        print("************* Bank Management Module **********")
        self.driver.get(self.baseURL)

        if self.driver.title == "GTPL Bank Home Page":
            assert True == True
            print("Home Page Title Test Passed")

    @pytest.mark.sanity
    def test_login(self):
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.lp.set_username(self.username)
        time.sleep(2)
        self.lp.set_password(self.password)
        time.sleep(2)
        self.lp.click_login()
        time.sleep(2)
        self.lp.set_newcustomer()
        time.sleep(2)
        self.lp.set_customername(self.customername)
        time.sleep(2)
        self.lp.click_gender()
        time.sleep(2)
        self.lp.set_dateofbirth(self.dateofbirth)
        time.sleep(2)
        print("********New Customer Module*********")
