"""
Author: Kasthuri
Description : Testing post function of an API
Running command:
        * pytest -v -s --html=.\reports\report.html --self-contained-html test_post_books.py
        * pytest test_put_books.py -v -s
        * pytest -m runpost -v -s

"""
# ************ Importing Libraries ********** #
import pytest
from http_operation.post_data_to_book import PostBook
import logging
import yaml

# ***************** program Starting ***********#
post_request = PostBook()
logger = logging.getLogger('Test Login')  # Logger


@pytest.mark.api
@pytest.mark.runpost
def test_add_new_book(create_data):
    """ Calling post method and adding new book """
    try:
        response = post_request.passing_payload_to_post_api(create_data)
        data = response
        logger.info(data)
        logger.info(" Payload passing successfully ")
    except:
        logger.exception("Passing payload get failed ")


@pytest.mark.api
@pytest.mark.runpost
def test_post_book_header_verification():
    """ Header verification for post book api """
    try:
        response_headverify = post_request.header_validation()
        logger.info(" Header verification done")
        return response_headverify

    except:
        logger.exception("Header verification failed ")


@pytest.mark.api
@pytest.mark.runpost
def test_post_book_statuscode_verify():
    """ Status code verification for post book api """
    try:
        status_response = post_request.status_code_verify()
        logger.info("Status code verification completed")
        return status_response
    except:
        logger.exception("Status code verification failed")

# ************* End of the program *********** #
