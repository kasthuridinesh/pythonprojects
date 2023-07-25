# ************ Importing Libraries ********** #
from json import dumps
from utils.request import APIRequest
from configuration.config import PUT, BASE, PUT_RESPONSE_CODE, PUT_HEADER_CONTENT
from http_operation.base_page import BaseClient
import urllib.parse
import logging

# ****************** Start of the program************* #

logger = logging.getLogger('Test Login')  # Logger


class Put_Book(BaseClient):
    """ creating class for put  book api """

    def __init__(self):
        super().__init__()
        self.header = None
        self.puturl = None
        self.base_url = BASE
        self.put_url = PUT
        self.request = APIRequest()
        self.response_code = PUT_RESPONSE_CODE
        self.content_type = PUT_HEADER_CONTENT

    def update_book(self, body=None):
        """ Updating book """
        response = self.__passing_payload_to_put_api(body)
        return response

    def __passing_payload_to_put_api(self, body=None):
        """ passing paylaod to put api"""
        if body is None:

            payload = dumps({
                "id": 0,
                "title": "string",
                "description": "string",
                "pageCount": 0,
                "excerpt": "string",
                "publishDate": "2023-02-16T04:51:18.264Z"

            })
        else:
            payload = dumps(body)
        self.puturl = urllib.parse.urljoin(self.base_url, self.put_url)
        response = self.request.put(self.puturl, payload, self.headers)
        self.statuscode = response.status_code
        self.header = response.headers
        logger.info(response.headers)
        return response

    def header_validation(self):
        """ Header verification for put book api """
        logger.info(self.header)
        content = str(self.header['Content-Type'])
        logger.info(content)
        assert content == self.content_type

    def status_code_verification(self):
        """ Status code verification for put book api """
        logger.info(self.statuscode)
        assert self.statuscode == 200
# ************* End of the program *********** #
