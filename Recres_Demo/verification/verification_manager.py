from utils.logger import get_logger
class Verify:
    # write assertion methods for string, number, boolean
    # write status code methods and response header methods
    # verify key - value  in response eg. email value we have to verify
    # for exp text, act data

    logger = get_logger()

    def verify_string(self,actual_text, expected_text, message): # from users_api
        try:
            assert actual_text == expected_text
            self.logger.info("Actual Result :: " + actual_text + "==" + "Ecpected Result :: " + str(expected_text))
        except:
            self.logger.info("String validation failed!")

    def verify_number(self, actual, expected, message): # for status code integer verftn
        print(message)
        try:
            assert actual == expected
            self.logger.info("Number validation is successful")
        except:
            self.logger.info("Number validation failed !")


    def verify_boolean(actual, expected, message):
        pass


