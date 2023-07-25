# ************ Importing Libraries ********** #
import urllib.parse
import requests
import logging
from utils.request import APIRequest
from http_operation.base_page import BaseClient
from configuration.config import BASE, DELETE, RESPONSE_CODE, DELETE_PARTICULAR_ID, DELETE1
# ****************** Start of the program************* #
logger = logging.getLogger('Test Login')  # Logger


class Delete_Book(BaseClient):
    """ Creating delete class """

    def __init__(self):
        super().__init__()

        self.delete_method = None
        self.response_code = RESPONSE_CODE
        self.geturl = None
        self.base_url = BASE
        self.delete = DELETE
        self.delete1 = DELETE1
        self.request = APIRequest()
        self.end_position = DELETE_PARTICULAR_ID

    def delete_book_url(self):
        """ Getting book url of delete api """
        self.delete_method = urllib.parse.urljoin(self.base_url, self.delete)
        return self.request.delete(self.delete_method)

    def delete_particular_book(self):
        """ Delete particular book by id """
        delete_endpoint = f'{self.delete1}{self.end_position}'
        self.geturl = urllib.parse.urljoin(BASE, delete_endpoint)
        return self.request.delete(self.geturl)

    def status_code_verification(self):
        """ Status code verification of delete API  """
        response = requests.delete(self.delete_method)
        logger.info(response.status_code)
        assert response.status_code == self.response_code
# ************* End of the program *********** #