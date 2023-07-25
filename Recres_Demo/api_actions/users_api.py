from api_handlers.http_handlers import HTTPHandler
from project_constants.api_keys import APIKeysConstants
from project_constants.constants import Constants
from utils import test_data_handler, test_utils
from utils.logger import get_logger
from verification.verification_manager import Verify

class UsersAPI:

    logger = get_logger()

    def verify_single_user_response(self):
        # dynamically generate id, use it in endpoint
        # individually put all json users in constants
        user_id = test_utils.get_random_number(1, 12)
        user_id_string = str(user_id)
        single_user_endpoint = Constants.SINGLE_USER_ENDPOINT.replace("[id]",user_id_string)
        response = HTTPHandler.make_get_api_call(self, single_user_endpoint)
        response_json = response.json()
        actual_response_data = response_json[APIKeysConstants.DATA_KEY]
        print(actual_response_data)

        expected_response_data = test_data_handler.get_user_by_id(user_id)
        print(expected_response_data)

        Verify.verify_number(self, actual_response_data, expected_response_data, "Verify user id")




        #return response # validate with key and value









