"""
Author: Kasthuri
Description : Defining methods for :
             Create, put, post, get methods for books api
"""
# ************ Importing Libraries ********** #
import json
import random
from datetime import datetime
from logging.handlers import HTTPHandler

import requests
from api_operations.validate_operations import Validation
from constants.api_constant import APIKeysConstants
# from constants.api_constant import APIKeysConstants
from constants.constants import *
from directory.global_directory import JSON_PATH
from utilities import test_data_handler, test_utils
from utilities.config_parser import ConfigReader
from utilities.logger import get_logger
from verification.verification_manager import BaseClient
from constants.messages import InfoMessages

#
# # ***************** program Starting ***********#
books_verify = BaseClient
class Books(Validation):
    """
    Creating class for   books swagger api
    """
    books_logger = get_logger()

    def __init__(self):
        self.base_url = BASE_URL

    def verify_single_user_response(self):
        # dynamically generate id, use it in endpoint
        # individually put all json users in constants
        global data_item
        endpoint = GET_BOOK_BY_ID_ENDPOINT
        user_id = test_utils.get_random_number(1, 200)
        user_id_string = str(user_id)
        single_user_endpoint = f'{endpoint}{user_id_string}'
        single_user_endpoint_final = requests.get(self.base_url + single_user_endpoint)
        single = single_user_endpoint_final.json()
        print(single)
        json_data = json.dumps(single)
        js = json.loads(json_data)
        actual_response_data = js[APIKeysConstants.ID_KEY]
        self.books_logger.info(actual_response_data)
        user_dict = test_data_handler.get_user_by_id(user_id)
        self.books_logger.info(user_dict)
        expected_response_data = user_dict[APIKeysConstants.ID_KEY]
        books_verify.verify_number(self , actual_response_data, expected_response_data, InfoMessages.VERIFY_ID_MESSAGE)

        # title verification
        actual_response_data = js[APIKeysConstants.TITLE]
        self.books_logger.info(actual_response_data)
        expected_response_data = user_dict[APIKeysConstants.TITLE]
        books_verify.verify_string(self, actual_response_data, expected_response_data, InfoMessages.VERIFY_TITLE_MESSAGE)




    def get_books(self):
        """
        This method is used to getting details of all books
        And verifying status code and header
        """
        try:
            endpoint = GET_BOOKS_ENDPOINT
            get_books = requests.get(self.base_url + endpoint)
            print(get_books.text)
            expected_status = EXPECTED_STATUS_CODE
            actual_status = get_books.status_code

            expected_header = EXPECTED_HEADER
            actual_header = get_books.headers["Content-Type"]
            print("This is getting data from get book api method:",actual_header)

            self.books_logger.info(actual_header)
            self.books_logger.info(actual_status)

            self.validate_status_code(actual_status, expected_status)
            self.books_logger.info("Status code verification is successful")

            self.validate_header(expected_header, actual_header)
            self.books_logger.info("Header  verification is successful")
            print("printing get data:",get_books.content)

        except:
            self.books_logger.exception("Get book api is unsuccessful")

    def create_book(self):
        """
        This method is used to create new book for books api
        And validating status code and header of created book
        """
        try:
            endpoint = CREATE_BOOKS_ENDPOINT
            json_data = self.generate_create_books_json_data()
            creating_book = requests.post(self.base_url + endpoint, json=json_data)
            ConfigReader.config_update_value("books", "id", creating_book.json()["id"])
            print("data passed at the time of creating book by id:",creating_book.text)

            expected_status = EXPECTED_STATUS_CODE
            actual_status_code = creating_book.status_code

            expected_header = EXPECTED_HEADER
            actual_header = creating_book.headers["Content-Type"]

            expected_integer = json_data["id"]
            actual_integer = json.loads(creating_book.text)["id"]

            expected_string = json_data["title"]
            actual_string = json.loads(creating_book.text)["title"]

            self.validate_status_code(actual_status_code, expected_status)
            self.books_logger.info("Status code verification is successful")

            self.validate_header(expected_header, actual_header)
            self.books_logger.info("Header  verification is successful")

            self.data_validation_integer(actual_integer, expected_integer)
            self.data_validation_string(actual_string, expected_string)



        except:

            self.books_logger.exception("Create book api is un-successful")

    def get_book_detail_by_id(self):
        """
        This method is used to getting book details by book_id
        Book id is generated randomly
        """
        try:
            endpoint = GET_BOOK_BY_ID_ENDPOINT
            book_id = ConfigReader.get_config_data("books", "id")
            get_book = requests.get(self.base_url + endpoint + "/" + str(book_id))

            expected_status = EXPECTED_STATUS_CODE
            actual_status = get_book.status_code

            expected_header = EXPECTED_HEADER
            actual_header = get_book.headers["Content-Type"]

            self.validate_status_code(actual_status, expected_status)
            self.books_logger.info("Status code verification is successful")

            self.validate_header(expected_header, actual_header)
            self.books_logger.info("Header  verification is successful")

        except:
            self.books_logger.exception("Get book by_id is un-successful")

    def update_book_details_by_id(self):
        """
        This method is used to updating book
        And validating status code and header for updated book
        """
        try:
            endpoint = UPDATE_BOOK_BY_ID_ENDPOINT
            book_id = ConfigReader.get_config_data("books", "id")
            payload = self.generate_create_books_json_data()
            update_book = requests.put(self.base_url + endpoint + "/" + str(book_id), json=payload)
            print("printing updated books details:",update_book.text)

            expected_status = EXPECTED_STATUS_CODE
            actual_status_code_for_update_book = update_book.status_code

            expected_header_for_update_book = EXPECTED_HEADER
            actual_header_for_update_book = update_book.headers["Content-Type"]

            expected_integer_data_for_update_book = payload["id"]
            actual_integer_data_for_update_book = json.loads(update_book.text)["id"]

            expected_string_data_for_update_book = payload["title"]
            actual_string_data_for_update_book = json.loads(update_book.text)["title"]

            self.validate_status_code(actual_status_code_for_update_book, expected_status)
            self.books_logger.info("Status code verification is successful")

            self.validate_header(expected_header_for_update_book, actual_header_for_update_book)
            self.books_logger.info("Header  verification is successful")

            self.data_validation_integer(actual_integer_data_for_update_book, expected_integer_data_for_update_book)
            self.data_validation_string(actual_string_data_for_update_book, expected_string_data_for_update_book)

        except:
            self.books_logger.exception("Update book by id is un-successful")

    def delete_book_by_id(self):
        """
        This method is used to delete a book by their book id
        And validating status code and header
        :return:
        """
        try:
            endpoint = DELETE_BOOK_BY_ID_ENDPOINT
            book_id = ConfigReader.get_config_data("books", "id")
            delete_book = requests.delete(self.base_url + endpoint + "/" + str(book_id))

            expected_status_code_for_delete_book = EXPECTED_STATUS_CODE
            actual_status_code_for_delete_book = delete_book.status_code

            self.validate_status_code(actual_status_code_for_delete_book, expected_status_code_for_delete_book)
            self.books_logger.info("Status code verification is successful")

        except:
            self.books_logger.exception("Deleting book by id is un-successful ")

    def generate_create_books_json_data(self):
        """
        This method is used to randomly generating book id
        :return: returning json data
        """
        try:
            self.books_logger.info("")
            with open(JSON_PATH, "r") as json_data:
                data = json.loads(json_data.read())
                # json_data.close()
            data["id"] = random.randint(1, 200)
            data["publishDate"] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            return data
        except:
            self.books_logger.exception("Generating data get failed")




# ************* End of the program ********
