from utils.logger import get_logger


class Verify:
    logger = get_logger()

    def verify_string(self, actual_text, expected_text, message):
        self.logger.info(message)
        try:
            assert actual_text == expected_text
            self.logger.info("PASS: Actual Result :: " + actual_text + " == " + "Expected Result :: " + expected_text)
        except AssertionError as error:
            self.logger.info("FAIL: Actual Result :: " + actual_text + " == " + "Expected Result :: " + expected_text, error)

    def verify_number(self, actual, expected, message):
        self.logger.info(message)
        try:
            assert actual == expected
            self.logger.info("PASS: Actual Result :: " + str(actual) + " == " + "Expected Result :: " + str(expected))
        except AssertionError as error:
            self.logger.info("FAIL: Actual Result :: " + str(actual) + " == " + "Expected Result :: " + str(expected), error)

    def verify_boolean(self, actual, expected, message):
        self.logger.info(message)
        try:
            assert actual == expected
            self.logger.info("PASS: Actual Result :: " + actual + " == " + "Expected Result :: " + expected)
        except AssertionError as error:
            self.logger.info("FAIL: Actual Result :: " + actual + " == " + "Expected Result :: " + expected, error)
