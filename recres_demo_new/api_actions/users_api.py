from pprint import pprint

from api_handlers.http_handlers import HTTPHandler
from project_constants.api_keys import APIKeysConstants
from project_constants.constants import Constants
from project_constants.messages import InfoMessages
from utils import test_data_handler, test_utils
from utils.logger import get_logger
from verification.verification_manager import Verify


class UsersAPI:
    logger = get_logger()

    def verify_single_user_response(self):
        user_id = test_utils.get_random_number_with_range(Constants.USER_ID_START, Constants.USER_ID_END)
        user_id_string = str(user_id)
        single_user_endpoint = Constants.SINGLE_USER_ENDPOINT.replace(Constants.ID_DYNAMIC_TEXT, user_id_string)
        response = HTTPHandler.make_get_api_call(self, single_user_endpoint)
        response_json = response.json()

        # Fetching 'data' key-values
        api_response_dict = response_json[APIKeysConstants.DATA_KEY]

        # Verifying User ID key-value
        actual_user_id = api_response_dict[APIKeysConstants.ID_KEY]
        user_dict = test_data_handler.get_user_by_id(user_id)
        pprint(user_dict)
        expected_user_id = user_dict[APIKeysConstants.ID_KEY]

        Verify.verify_number(self, actual_user_id, expected_user_id, InfoMessages.VERIFY_ID_MESSAGE)

        # Verifying Email key-value
        actual_email_id = api_response_dict[APIKeysConstants.EMAIL_KEY]

        expected_email_id = user_dict[APIKeysConstants.EMAIL_KEY]

        Verify.verify_string(self, actual_email_id, expected_email_id, InfoMessages.VERIFY_EMAIL_MESSAGE)

        # Verifying First Name key-value
        actual_first_name = api_response_dict[APIKeysConstants.FIRST_NAME_KEY]

        expected_first_name = user_dict[APIKeysConstants.FIRST_NAME_KEY]

        Verify.verify_string(self, actual_first_name, expected_first_name, InfoMessages.VERIFY_FIRST_NAME_MESSAGE)

        # Verifying Last Name key-value
        actual_last_name = api_response_dict[APIKeysConstants.LAST_NAME_KEY]

        expected_last_name = user_dict[APIKeysConstants.LAST_NAME_KEY]

        Verify.verify_string(self, actual_last_name, expected_last_name, InfoMessages.VERIFY_LAST_NAME_MESSAGE)

        # Verifying Avatar key-value
        actual_avatar = api_response_dict[APIKeysConstants.AVATAR_KEY]

        expected_avatar = user_dict[APIKeysConstants.AVATAR_KEY]

        Verify.verify_string(self, actual_avatar, expected_avatar, InfoMessages.VERIFY_AVATAR_MESSAGE)
        print("--------------------------------------------------------------------")
        #
        # # Fetching 'support' key-values
        # api_response_dict = response_json[APIKeysConstants.SUPPORT_KEY]
        # user_dict = test_data_handler.get_user_by_key("support")
        #
        # actual_support_url = api_response_dict[APIKeysConstants.URL_KEY]
        #
        # expected_support_url = user_dict[APIKeysConstants.URL_KEY]
        #
        # Verify.verify_string(self, actual_support_url, expected_support_url, InfoMessages.VERIFY_SUPPORT_URL_MESSAGE)
        #
        # # Verifying 'support' Text key-value
        # actual_support_text = api_response_dict[APIKeysConstants.TEXT_KEY]
        #
        # expected_support_text = user_dict[APIKeysConstants.TEXT_KEY]
        #
        # Verify.verify_string(self, actual_support_text, expected_support_text, InfoMessages.VERIFY_SUPPORT_TEXT_MESSAGE)
        #

