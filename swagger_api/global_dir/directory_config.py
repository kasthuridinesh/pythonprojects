# ************ Importing Libraries ********** #

import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
POST_JSON = os.path.join(ROOT_DIR, "data/post.json")
PUT_JSON = os.path.join(ROOT_DIR, "data/put.json")
LOGGER_PATH = os.path.join(ROOT_DIR, "logs")
LOGGING_YAML_FILE_PATH = os.path.join(ROOT_DIR, "configuration/logging.yaml")
LOGGER_FILE_NAME = os.path.join(ROOT_DIR, "logs/automation.log")
