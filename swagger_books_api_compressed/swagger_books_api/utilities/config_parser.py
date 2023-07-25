import configparser

from directory import global_directory


class ConfigReader:
    """
    Update and get value from properties file
    """

    @staticmethod
    def config_update_value(section, key, value):
        """
        Update value in properties file
        :param section: valid section name in properties.ini
        :param key: valid key under given section in properties.ini
        :param value: valid value under given section in properties.ini
        """
        config = configparser.RawConfigParser()
        config.read(global_directory.PROPERTIES_FILE_PATH)
        config.set(section, key, value)
        with open(global_directory.PROPERTIES_FILE_PATH, 'w') as configfile:
            config.write(configfile)
            configfile.close()

    @staticmethod
    def get_config_data(section, key):
        """
        Get value from properties file
        :param section: valid section name in properties.ini
        :param key: valid key under given section in properties.ini foe rhich value to be fetched
        :return: Value for the key given
        """
        config = configparser.RawConfigParser()
        config.read(global_directory.PROPERTIES_FILE_PATH)
        value = config.get(section, key)
        return value
