# ************ Importing Libraries ********** #
from json import dumps
import logging
from utils.request import APIRequest
from configuration.config import POST, BASE, RESPONSE_CODE_POST, POST_CONTENT_TYPE
from http_operation.base_page import BaseClient
import urllib.parse
# ****************** Start of the program************* #
logger = logging.getLogger('Test Login')  # Logger


class PostBook(BaseClient):
    """ Creating class for post book api"""

    def __init__(self):
        super().__init__()

        self.geturl = None
        self.post_url = POST
        self.base_url = BASE
        self.request = APIRequest()
        self.response_code = RESPONSE_CODE_POST
        self.content_type = POST_CONTENT_TYPE

    def passing_payload_to_post_api(self, body=None):
        """ Passing payload if no data is found in json file """
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
            self.posturl = urllib.parse.urljoin(self.base_url, self.post_url)
            response = self.request.post(self.posturl, payload, self.headers)
            self.statuscode = response.status_code
            self.header = response.headers
            return response

    def header_validation(self):
        """ Validating header for post book api """
        logger.info(self.header)
        content = str(self.header['Content-type'])
        logger.info(content)
        assert content == self.content_type

    def status_code_verify(self):
        """ Status code verification of post api"""
        logger.info(self.statuscode)
        assert self.statuscode == 200
# ************* End of the program *********** #