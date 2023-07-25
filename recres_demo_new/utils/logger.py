import os
import logging
from directory.global_directory import LOGGER_FILE_PATH


def get_logger():
    if not os.path.exists(LOGGER_FILE_PATH):
        os.makedirs(LOGGER_FILE_PATH)
    log_file = "reqres_api_automation.log"
    log_path = os.path.join(LOGGER_FILE_PATH, log_file)
    logging.basicConfig(
        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
        level=logging.INFO,
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )                # use yaml file and setup everything

    return logging.getLogger()