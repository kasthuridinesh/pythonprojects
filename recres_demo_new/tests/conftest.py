import pytest

from api_actions.users_api import UsersAPI
from verification.verification_manager import Verify


@pytest.fixture(autouse=True)
def api_modules():
    users = UsersAPI()
    verify = Verify()