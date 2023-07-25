import json
import random
from datetime import datetime

import requests

from api_operations.validate_operations import Validations
from constants.constants import *
from directory.global_directory import JSON_PATH
from utilities.config_parser import ConfigReader
from utilities.logger import get_logger


class Books(Validations):
    books_logger = get_logger()

    def __init__(self):
        self.base_url = BASE_URL

    def get_books(self):
        endpoint = GET_BOOKS_ENDPOINT
        response = requests.get(self.base_url + endpoint)
        expected_status_code = EXPECTED_STATUS_CODE
        actual_status_code = response.status_code
        expected_header = EXPECTED_HEADER
        actual_header = response.headers["Content-Type"]
        self.validate_status_code(actual_status_code, expected_status_code)
        self.validate_header(expected_header, actual_header)

    def create_book(self):
        endpoint = CREATE_BOOKS_ENDPOINT
        json_data = self.generate_create_books_json_data()
        response = requests.post(self.base_url + endpoint, json=json_data)
        expected_status_code = EXPECTED_STATUS_CODE
        actual_status_code = response.status_code
        expected_header = EXPECTED_HEADER
        actual_header = response.headers["Content-Type"]
        self.validate_status_code(actual_status_code, expected_status_code)
        self.validate_header(expected_header, actual_header)
        ConfigReader.config_update_value("books", "id", response.json()["id"])

    def get_book_detail_by_id(self):
        endpoint = GET_BOOK_BY_ID_ENDPOINT
        book_id = ConfigReader.get_config_data("books", "id")
        response = requests.get(self.base_url + endpoint + "/" + str(book_id))
        expected_status_code = EXPECTED_STATUS_CODE
        actual_status_code = response.status_code
        expected_header = EXPECTED_HEADER
        actual_header = response.headers["Content-Type"]
        self.validate_status_code(actual_status_code, expected_status_code)
        self.validate_header(expected_header, actual_header)

    def update_book_details_by_id(self):
        endpoint = UPDATE_BOOK_BY_ID_ENDPOINT
        book_id = ConfigReader.get_config_data("books", "id")
        payload = self.generate_create_books_json_data()
        response = requests.put(self.base_url + endpoint + "/" + str(book_id), json=payload)
        expected_status_code = EXPECTED_STATUS_CODE
        actual_status_code = response.status_code
        expected_header = EXPECTED_HEADER
        actual_header = response.headers["Content-Type"]
        self.validate_status_code(actual_status_code, expected_status_code)
        self.validate_header(expected_header, actual_header)

    def delete_book_by_id(self):
        endpoint = DELETE_BOOK_BY_ID_ENDPOINT
        book_id = ConfigReader.get_config_data("books", "id")
        response = requests.delete(self.base_url + endpoint + "/" + str(book_id))
        expected_status_code = EXPECTED_STATUS_CODE
        actual_status_code = response.status_code
        self.validate_status_code(actual_status_code, expected_status_code)

    def generate_create_books_json_data(self):
        self.books_logger.info("")
        with open(JSON_PATH, "r") as json_data:
            data = json.loads(json_data.read())
            json_data.close()
        data["id"] = random.randint(1, 200)
        data["publishDate"] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return data


obj = Books()
obj.get_books()
obj.create_book()
obj.get_book_detail_by_id()
obj.update_book_details_by_id()
obj.delete_book_by_id()
