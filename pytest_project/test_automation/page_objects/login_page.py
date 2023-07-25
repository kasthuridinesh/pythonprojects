from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page xpath's
    textbox_username_xpath = "//input[@name='uid']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//input[@name='btnLogin']"
    button_reset_xpath = "//input[@name='btnReset']"
    new_customer_button = "New Customer"
    textbox_customer_name = "//input[@name='name']"
    radio_button_gender = "//input[@name='rad1']"
    select_dateofbirth = "dob"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_reset(self):
        self.driver.find_element(By.XPATH, self.button_reset_xpath).click()

    def set_newcustomer(self):
        self.driver.find_element(By.LINK_TEXT, self.new_customer_button).click()

    def set_customername(self, customername):
        self.driver.find_element(By.XPATH, self.textbox_customer_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_customer_name).send_keys(customername)

    def click_gender(self):
        self.driver.find_element(By.XPATH, self.radio_button_gender).click()

    def set_dateofbirth(self,dateofbirth):
        self.driver.find_element(By.NAME, self.select_dateofbirth).clear()
        self.driver.find_element(By.NAME, self.select_dateofbirth).send_keys(dateofbirth)

