import configparser

from test_automation.configuration import file_path_constants

config = configparser.RawConfigParser()
config.read(file_path_constants.CONFIG_FILE_PATH)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = (config.get('common_info', 'baseURL'))
        return url

    @staticmethod
    def get_username():
        username = (config.get('common_info', 'username'))
        return username

    @staticmethod
    def get_password():
        password = (config.get('common_info', 'password'))
        return password

    @staticmethod
    def get_customername():
        customername = (config.get('common_info', 'customername'))
        return customername

    @staticmethod
    def get_dateofbirth():
        dateofbirth = (config.get('common_info', 'dateofbirth'))
        return dateofbirth

