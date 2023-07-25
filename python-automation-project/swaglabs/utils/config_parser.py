import configparser
from swaglabs.globals import dir_global

config = configparser.RawConfigParser()
config.read(dir_global.INI_CONFIGS_PATH)


class ConfigParserIni:
    @staticmethod
    def get_application_url():
        url = (config.get('Base Url', 'base_url'))
        return url

    @staticmethod
    def get_username():
        username = (config.get('Base Url', 'username'))
        return username

    @staticmethod
    def get_password():
        password = (config.get('Base Url', 'password'))
        return password

    @staticmethod
    def get_homepage_url():
        home_url = (config.get('Base Url', 'homepage_url'))
        return home_url

    @staticmethod
    def get_firstname():
        firstname = (config.get('Add Cart', 'firstname'))
        return firstname

    @staticmethod
    def get_lastname():
        lastname = (config.get('Add Cart', 'lastname'))
        return lastname

    @staticmethod
    def get_pincode():
        pincode = (config.get('Add Cart', 'pincode'))
        return pincode
