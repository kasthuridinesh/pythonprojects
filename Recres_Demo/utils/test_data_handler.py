from project_constants.api_keys import APIKeysConstants
from utils.file_handler import JSONFileHandler


def get_user_by_id(user_id):
    json_file_handler = JSONFileHandler("C:/Users/kasthuri.kandavelu/PycharmProjects/Recres_Demo/tests_data/api_response_data/single_user_response.json")
    user_data = json_file_handler.get_value_by_key(APIKeysConstants.DATA_KEY)
    for dict in user_data:
        if dict[APIKeysConstants.ID_KEY] == user_id:
            return dict


