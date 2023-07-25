from project_constants.api_keys import APIKeysConstants
from project_constants.constants import FilePathConstants
from utils.file_handler import JSONFileHandler


def get_user_by_id(user_id):
    json_file_handler = JSONFileHandler(FilePathConstants.SINGLE_USER_RESPONSE_FILE)
    user_data = json_file_handler.get_value_by_key(APIKeysConstants.DATA_KEY)
    for user_dict in user_data:
        if user_dict[APIKeysConstants.ID_KEY] == user_id:
            return user_dict

# def get_user_by_key(key):
#     json_file_handler = JSONFileHandler(FilePathConstants.SINGLE_USER_RESPONSE_FILE)
#     user_data = json_file_handler.get_value_by_key(APIKeysConstants.SUPPORT_KEY)
#     for user_dict in user_data:
#         if user_dict[APIKeysConstants.URL_KEY] == key:
#             return user_dict
