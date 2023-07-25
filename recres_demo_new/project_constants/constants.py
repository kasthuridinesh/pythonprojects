
class Constants:
    ID_DYNAMIC_TEXT = "[id]"
    USER_ID_START = 1
    USER_ID_END = 12

    # API URL related constants
    BASE_URL = "https://reqres.in/api"

    SINGLE_USER_ENDPOINT = f"{BASE_URL}/users/{ID_DYNAMIC_TEXT}"


class FilePathConstants:

    RESPONSE_TEST_DATA_HOME = "tests_data/api_response_data/"

    SINGLE_USER_RESPONSE_FILE = RESPONSE_TEST_DATA_HOME + "single_user_response.json"

    REQUEST_TEST_DATA_HOME = "tests_data/api_request_data/"

