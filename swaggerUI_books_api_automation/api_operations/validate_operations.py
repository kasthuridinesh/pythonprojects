# ************ Importing Libraries ********** #
from utilities.logger import get_logger


# ***************** program Starting ***********#
import json

import requests

from utilities.logger import get_logger


class Validation():
    """
    Creating class for validating api
    """
    books_logger = get_logger()

    def validate_status_code(self, actual_status_code, expected_status_code):
        """
    This method is used to validating expected status code with actual
    :param actual_status_code:fetching from response
    :param expected_status_code:comparing the data need to be checked
    """
        print("printing actual status code:", actual_status_code)
        print("printing expected status code:", expected_status_code)
        try:
            assert actual_status_code == expected_status_code
            self.books_logger.info("Status code verification successful")
        except:
            self.books_logger.exception("Status code verification failed")

    def validate_header(self, expected_header, actual_header):
        """
    This method is used to validating expected header with actual header
    :param expected_header:comparing the data need to be checked
    :param actual_header: fetching from response

    """

        try:
            assert expected_header in actual_header
            self.books_logger.info("header verification done")

        except:
            self.books_logger.exception("Header verification failed")

    def data_validation_integer(self, actual_integer_data, expected_integer_data):
        """
        Method for validating integer
        """
        print("printing actual integer data:", actual_integer_data)
        print("printing expected integer data:", expected_integer_data)
        try:
            assert actual_integer_data == expected_integer_data
            self.books_logger.info(
                "Actual Result :: " + str(actual_integer_data) + " == " + " Expected Result :: " + str(
                    expected_integer_data))

            self.books_logger.info("data validation for integer data expected")
            self.books_logger.info("payload integer passed successfully passed")
        except:
            self.books_logger.exception("Data validation failed")

    def data_validation_string(self, actual_string_data, expected_string_data):
        """
        Verifying string data with actual and expected
        """
        try:
            assert actual_string_data == expected_string_data
            self.books_logger.info("Actual Result :: " + actual_string_data + " == " + " Expected Result :: " + str(
                expected_string_data))
            self.books_logger.info("String data validation successful")
        except:
            self.books_logger.exception("String validation failed")

# # ************* End of the program *********** #
