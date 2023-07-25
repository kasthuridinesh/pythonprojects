import json
from global_dir.directory_config import PUT_JSON
BASE_PATH =PUT_JSON


def read(file_name):
    with open(BASE_PATH, mode='r') as f:
        return json.load(f)
