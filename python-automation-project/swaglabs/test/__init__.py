import os

import yaml
import logging.config

from swaglabs.globals import dir_global
from swaglabs.configuration.yaml_file_constants import yaml_handlers, yaml_file, yaml_filename

config_dict = None


def yaml_config(yaml_file_, name):
    with open(yaml_file_) as file:
        global config_dict
        config_dict = yaml.safe_load(file)
        log_filename = name
        config_dict[yaml_handlers][yaml_file][yaml_filename] = log_filename

        # Apply the configuration
        return logging.config.dictConfig(config_dict)


log_file_path = os.path.join(dir_global.LOGGER_PATH, dir_global.LOGGER_FILE_NAME)
yaml_file_path = dir_global.LOGGING_YAML_FILE_PATH
yaml_config(yaml_file_path, log_file_path)
