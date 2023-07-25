"""
Author: Kasthuri
Description : Testing update function of an API
Running command:
        * pytest -v -s --html=.\reports\report.html --self-contained-html test_put_books.py
        * pytest test_put_books.py -v -s
        * pytest -m runput -v -s

"""
# ************ Importing Libraries ********** #
import logging
import pytest
from http_operation.update_particular_book import Put_Book

# ***************** program Starting ***********#
put_request = Put_Book()
logger = logging.getLogger('Test Login')  # Logger


@pytest.mark.api
@pytest.mark.runput
def test_update_book(create_put):
    """ Calling put method and update the book """
    try:
        response = put_request.update_book(create_put)
        put_data = response
        #  printing updated book details
        logger.info(put_data)
        logger.info("Update new book successfully done")
    except:
        logger.exception("New book updation failed")


@pytest.mark.api
@pytest.mark.runput
def test_update_book_header_verification():
    """ Header verification for put  book api """
    try:
        response_header_verify = put_request.header_validation()
        logger.info("Header verification done")
        return response_header_verify
    except:
        logger.exception("Header verification failed")


@pytest.mark.api
@pytest.mark.runput
def test_updatebook_statuscode_verify():
    """ Status code verification for put api"""
    try:
        status_response = put_request.status_code_verification()
        logger.info("Update status code verification done ")
        return status_response
    except:
        logger.exception("Update status code verification failed")

# ************* End of the program *********** #
