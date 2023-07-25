import pytest
from api_actions.users_api import UsersAPI
import allure
from project_constants.messages import VerificationMessages
from utils.logger import get_logger

users = UsersAPI()


@pytest.mark.run
class TestUsers:
    logger = get_logger()

    @allure.title("Test Single User API in reqres.in")
    @allure.description("This test case is about testing the single user response dynamically for any user in the pages")
    def test_single_user_api(self):
        self.logger.info(VerificationMessages.SINGLE_USER_VERIFICATION_START_MESSAGE)
        users.verify_single_user_response()
        self.logger.info(VerificationMessages.SINGLE_USER_VERIFICATION_STOP_MESSAGE)
