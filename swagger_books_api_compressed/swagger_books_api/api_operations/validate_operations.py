from utilities.logger import get_logger


class Validations():
    books_logger = get_logger()

    def validate_status_code(self, actual_status_code, expected_status_code):
        self.books_logger.info("")
        assert actual_status_code == expected_status_code

    def validate_header(self, expected_header, actual_header):
        self.books_logger.info("")
        assert expected_header in actual_header
