"""
Author: Kasthuri
Description : Testing get1 function of an API
Running command:
        * pytest -v -s --html=.\reports\report.html --self-contained-html test_get1_books.py
        * pytest test_put_books.py -v -s
        * pytest -m runget1 -v -s



"""
# ************ Importing Libraries ********** #
import logging
import pytest
from http_operation.get_book import Get1_book

# ***************** program Starting ***********#
get_request = Get1_book()
logger = logging.getLogger('Test Login')  # Logger


@pytest.mark.api
@pytest.mark.runget1
def test_book_url(create_data):
    """ Calling url method for get api """
    try:
        response_url = get_request.get1_book_url()
        data_get = response_url.as_dict
        logger.info(data_get)
        assert response_url.status_code== 200
        logger.info(" Url verification done ")
        return response_url

    except:
        logger.exception("please enter valid API")


@pytest.mark.api
@pytest.mark.runget1
def test_book_header_verification():
    """ Calling url method for get api """
    try:
        response_headerverify = get_request.get1book_header_validation()
        logger.info("Header verification completed ")
        return response_headerverify
    except:
        logger.exception("header of both response and request not match")


@pytest.mark.api
@pytest.mark.runget1
def test_book_statuscode_verify():
    """ Verifying status code for get1book API  """
    try:
        status_response = get_request.get1book_status_code_verify()
        logger.info("Status code verification completed ")
        return status_response
    except:
        logger.exception("Status code of response is not valid")

# ************* End of the program *********** #
