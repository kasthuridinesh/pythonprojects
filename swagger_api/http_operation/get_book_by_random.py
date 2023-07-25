# ************ Importing Libraries ********** #
import random

import requests
import logging
from utils.request import APIRequest
from configuration.config import BASE, GET2, RESPONSE_CODE, CONTENT_TYPE
from http_operation.base_page import BaseClient
import urllib.parse
# ****************** Start of the program************* #
logger = logging.getLogger('Test Login')  # Logger


class Get2_Book(BaseClient):
    """Creating class for get2 book api """
    def __init__(self):
        super().__init__()

        self.geturl = None
        self.get_method_url = None
        self.base_url = BASE
        self.get2_books = GET2
        self.response_code = RESPONSE_CODE
        self.validate_content = CONTENT_TYPE
        self.request = APIRequest()

    def get_random_book(self):
        """ Verifying url of particular book from get2 api"""
        for id in range(123, 130,2):
            id = random.choice(range(123, 130, 2))
            endpoint = f'{self.get2_books}{id}'
            self.geturl = urllib.parse.urljoin(BASE, endpoint)
            response = requests.get(self.geturl)
            logger.info(response.text)
    # def get_random_book(self):
    #     """ Verifying url of particular book from get2 api"""
    #     id = random.choice(range(123, 130, 2))
    #     endpoint = f'{self.get2_books}{id}'
    #     expected_url = urllib.parse.urljoin(BASE, endpoint)
    #     response = requests.get(expected_url)
    #     logger.info(response.text)
    #     assert response.url == expected_url, f"Unexpected URL: {response.url}"

    def get2_books_header_validation(self):
        """ Header verification of get2 api"""
        response = requests.get(self.geturl)
        hearders = response.headers
        content_type = str(hearders['Content-type'])
        logger.info(content_type)
        assert content_type == CONTENT_TYPE

    def get2_book_status_code_verification(self):
        """Verifying status code verification for get2 api"""
        response = requests.get(self.geturl)
        logger.info(response.status_code)
        assert response.status_code == self.response_code

# ************* End of the program *********** #