from constants.api_constant import APIKeysConstants
from utilities.file_handlers import JSONFileHandler


def get_book_by_id(book_id):
    json_file_handler = JSONFileHandler(
        "//test_data/api_response_data/books_response.json")
    book_data = json_file_handler.get_value_by_key(APIKeysConstants.DATA_KEY)
    for dict in book_data:
        if dict[APIKeysConstants.ID_KEY] == book_id:
            return dict
