import configparser
from swaglabs.globals import dir_global

config = configparser.RawConfigParser()
config.read(dir_global.LOCATORS_CONFIGS_PATH)


class LocatorConfig:
    """Login page locators Configuration"""

    @staticmethod
    def get_login_user_name():
        login_user = (config.get('Login Button', 'USERNAME_FIELD'))
        return login_user

    @staticmethod
    def get_login_password():
        login_password = (config.get('Login Button', 'PASSWORD_FIELD'))
        return login_password

    @staticmethod
    def get_login_button():
        login_button = (config.get('Login Button', 'LOGIN_BUTTON'))
        return login_button

    @staticmethod
    def get_login_pagetitle():
        page_title = (config.get('Login Button', 'PAGE_TITLE'))
        return page_title

    @staticmethod
    def get_logout_button():
        logout_button = (config.get('Login Button', 'LOGOUT_BUTTON'))
        return logout_button

    """Menu Page Locator configuration Exercise 1"""

    @staticmethod
    def get_menu_button():
        menu_button = (config.get('Menu Button', 'MENU_BUTTON'))
        return menu_button

    @staticmethod
    def get_menu_allitem():
        menu_allitem = (config.get('Menu Button', 'ALL_ITEM'))
        return menu_allitem

    @staticmethod
    def get_menu_about():
        menu_about = (config.get('Menu Button', 'ABOUT'))
        return menu_about

    @staticmethod
    def get_menu_logout():
        menu_logout = (config.get('Menu Button', 'LOGOUT_BUTTON'))
        return menu_logout

    @staticmethod
    def get_menu_resetapp():
        menu_reset = (config.get('Menu Button', 'RESET_APP'))
        return menu_reset

    @staticmethod
    def get_menu_addcart():
        menu_addcart = (config.get('Menu Button', 'ADD_TO_CART'))
        return menu_addcart

    @staticmethod
    def get_menu_addcart_checkout():
        menu_add_checkout = (config.get('Menu Button', 'CHECK_OUT_BUTTON'))
        return menu_add_checkout

    """Product Page Locator configuration Exercise 2"""

    @staticmethod
    def get_product_addcart():
        product_addcart = (config.get('Product Page Button', 'ADD_TO_CART'))
        return product_addcart

    @staticmethod
    def get_product_checkout():
        product_checkout = (config.get('Product Page Button', 'CHECK_OUT_BUTTON'))
        return product_checkout

    @staticmethod
    def get_product_lowest_product_add():
        product_lowest_add = (config.get('Product Page Button', 'LOWEST_PRODUCT_ADD'))
        return product_lowest_add

    @staticmethod
    def get_product_firstname():
        product_firstname = (config.get('Product Page Button', 'FIRST_NAME'))
        return product_firstname

    @staticmethod
    def get_product_lastname():
        product_lastname = (config.get('Product Page Button', 'LAST_NAME'))
        return product_lastname

    @staticmethod
    def get_product_pincode():
        product_postalcode = (config.get('Product Page Button', 'POSTAL_CODE'))
        return product_postalcode

    @staticmethod
    def get_product_customer_checkout():
        product_customer_checkout = (config.get('Product Page Button', 'CUSTOMER_DETAILS_CHECKOUT_BUTTON'))
        return product_customer_checkout

    @staticmethod
    def get_product_finish_button():
        product_finish_button = (config.get('Product Page Button', 'FINAL_FINISH_BUTTON'))
        return product_finish_button

    """Product View Locator configuration Exercise 3"""

    @staticmethod
    def get_product_view_add_button():
        product_view_add_button = (config.get('Product View Button', 'add_product_button'))
        return product_view_add_button

    @staticmethod
    def get_product_view_click_productname():
        product_click_product_name = (config.get('Product View Button', 'click_product_name'))
        return product_click_product_name

    @staticmethod
    def get_product_view_name_details():
        product_view_productname = (config.get('Product View Button', 'product_detail_page_name'))
        return product_view_productname

    @staticmethod
    def get_product_view_price_details():
        product_view_productprice = (config.get('Product View Button', 'product_detail_page_price'))
        return product_view_productprice

    @staticmethod
    def get_product_view_image_details():
        product_view_productimage = (config.get('Product View Button', 'product_detail_page_image'))
        return product_view_productimage

    @staticmethod
    def get_product_view_remove_button():
        product_view_remove_button = (config.get('Product View Button', 'product_detail_page_remove_button'))
        return product_view_remove_button
