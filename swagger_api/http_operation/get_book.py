# ************ Importing Libraries ********** #
import urllib.parse
import logging
import requests
from http_operation.base_page import BaseClient
from configuration.config import BASE, GET1, RESPONSE_CODE, CONTENT_TYPE
from utils.request import APIRequest
# ****************** Start of the program************* #
logger = logging.getLogger('Test Login')


class Get1_book(BaseClient):
    """Creating class for get1 book API"""

    def __init__(self):
        super().__init__()

        self.geturl = None
        self.base_url = BASE
        self.get1 = GET1
        self.response_code = RESPONSE_CODE
        self.validate_content = CONTENT_TYPE
        self.request = APIRequest()

    def get1_book_url(self):
        """Getting all book url """
        self.geturl = urllib.parse.urljoin(self.base_url, self.get1)
        response = requests.get(self.geturl)
        logger.info(response.text)
        logger.info(response.status_code)
        return self.request.get(self.geturl)

    def get1book_header_validation(self):
        """ Validating header for all book of get1 API """
        response = requests.get(self.geturl)
        hearders = response.headers
        content_type = str(hearders['Content-type'])
        logger.info(content_type)
        assert content_type == self.validate_content

    def get1book_status_code_verify(self):
        """ Verifying status code of book get1 API """
        response = requests.get(self.geturl)
        logger.info(response.status_code)
        assert response.status_code == self.response_code
# ************* End of the program *********** #