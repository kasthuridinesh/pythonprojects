from selenium.webdriver.common.by import By
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def send_values(self, locator, val):
        self.driver.find_element(By.XPATH, locator).send_keys(val)
        return

    def click_button(self,locator):
        self.driver.find_element(By.XPATH, locator).click()
        return

    def scroll_down_funtion(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return

    def scroll_up_funtion(self):
        self.driver.execute_script("window.scroll(0, 0);")
        return

    def get_text(self, locator):
        var = self.driver.find_element(By.XPATH, locator).text
        return print(var)

    def display_details(self, locator):
        var = self.driver.find_element(By.XPATH, locator).is_displayed()
        return print(var)
