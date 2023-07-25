import time
from pytest_bdd import parsers, scenarios, then
from pytest_bdd import given
from pytest_bdd import when
from petstore_image.libs.sign_in import SignUp

scenarios('../feature_file/image_url.feature')


@given(parsers.parse("user launches the pets store application"))
def launch_url(browser):
    sign_up_page = SignUp(browser)
    sign_up_page.launch_url()


@when("user clicks on the signin in the pets store application")
def sign_in(browser):
    sign_up_page = SignUp(browser)
    sign_up_page.click_on_sign_in()


@when("user enters the valid username")
def username_field(browser):
    sign_up_page = SignUp(browser)
    time.sleep(2)
    sign_up_page.enter_username()


@when("user enters the valid password")
def username_field(browser):
    sign_up_page = SignUp(browser)
    time.sleep(3)
    sign_up_page.enter_password()


@then("user clicks on login button")
def username_field(browser):
    sign_up_page = SignUp(browser)
    sign_up_page.click_login_button()
    time.sleep(3)
