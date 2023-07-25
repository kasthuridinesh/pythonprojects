import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from petstore_image.constants.credentials import URL, USERNAME, PASSWORD
from petstore_image.constants.image_url import PET_IMAGE_URLS
from petstore_image.libs.driver_commands import BasicActions


class SignUp(BasicActions):
    base_url = URL

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.signup_link = "//a[text()='Sign In']"
        self.username_field = "//input[@name='username']"
        self.password_field = "//input[@name='password']"
        self.login_button = "//input[@name='signon']"

    def launch_url(self):
        self.get_url(self.base_url)

    def click_on_sign_in(self):
        self.click_by_xpath(self.signup_link)

    def enter_username(self):
        self.clear_by_xpath(self.username_field)
        self.type_by_xpath(self.username_field, USERNAME)

    def enter_password(self):
        self.clear_by_xpath(self.password_field)
        self.type_by_xpath(self.password_field, PASSWORD)

    def click_login_button(self):
        self.click_by_xpath(self.login_button)

    def select_random_image_url(self):
        try:
            selected_url = random.choice(PET_IMAGE_URLS)
            image_element = self.driver.find_element(By.XPATH, f"//img[@src='{selected_url}']")
            assert image_element.is_displayed()
            return selected_url
        except NoSuchElementException:
            pass
