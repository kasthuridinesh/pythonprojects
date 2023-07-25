from utilities.logger import get_logger


class BaseClient:
    books_logger = get_logger()

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def verify_number(self, actual, expected, message):  # for status code integer verftn
        self.books_logger.info(message)
        try:
            assert actual == expected
            self.books_logger.info("Number validation is successful")
        except:
            self.books_logger.info("Number validation failed !")

    def verify_string(self, actual_text, expected_text, message):  # for status code string verification
        self.books_logger.info(message)
        try:
            assert actual_text == expected_text
            self.books_logger.info(
                "PASS: Actual Result :: " + actual_text + " == " + "Expected Result :: " + expected_text)
        except AssertionError as error:
            self.books_logger.info(
                "FAIL: Actual Result :: " + actual_text + " == " + "Expected Result :: " + expected_text, error)
