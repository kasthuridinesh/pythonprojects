import pytest
import requests
import json
from api_actions.users_api import UsersAPI

from project_constants.messages import Messages
# from tests_data.api_response_data import
# from tests_data.api_response_data.single_user_response import SINGLE_USER_RESPONSE
from verification.verification_manager import Verify

users = UsersAPI()


class TestUsers:

    def test_single_user_api(self):
        users.verify_single_user_response()

        # assert response.status_code == 200
        # assert response.json()['data']['id'] == 2, f"the expected id is not found"
        # assert response.headers["Content-Type"] == "application/json"
        # string matching not good practise for response assertion
        # write helper method logic for validating all response keys values

# assert response.status_code == requests.codes.ok, Messages.API_RESPONSE_ERROR
#        assert json.loads(response.text) == SINGLE_USER_RESPONSE, Messages.API_RESPONSE_INCORRECT_DATA
