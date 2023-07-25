from json import dumps
from uuid import uuid4

from config.base_uri import BASE_URI
from http_methods.base_page import BaseClient
from utils.request import APIRequest


class PeopleClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_person(self, body=None):
        last_name, response = self.__create_person_with_unique_last_name(body)
        return last_name, response

    def __create_person_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'User {str(uuid4())}'
            payload = dumps({
                'fname': 'New',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return last_name, response
