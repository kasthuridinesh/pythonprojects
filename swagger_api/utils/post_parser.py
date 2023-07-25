# ************ Importing Libraries ********** #

import json
from global_dir.directory_config import POST_JSON

BASE_PATH = POST_JSON


def read_file(file_name):
    """ Reading json data from file and loading data"""
    with open(BASE_PATH, mode='r') as f:
        return json.load(f)
