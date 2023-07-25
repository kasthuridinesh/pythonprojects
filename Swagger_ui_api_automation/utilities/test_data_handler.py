from constants.api_constant import APIKeysConstants
from utilities.file_handlers import JSONFileHandler

def get_user_by_id(user_id):
    json_file_handler = JSONFileHandler("C:/Users/kasthuri.kandavelu/PycharmProjects/swagger_books_api/test_data/api_response_data/books_response.json")
    user_data = json_file_handler.get_value_by_key(APIKeysConstants.DATA_KEY)
    for dict in user_data:
        if dict[APIKeysConstants.ID_KEY] == user_id:
            return dict