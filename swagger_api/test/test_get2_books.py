"""
Author: Kasthuri
Description : Testing get2 function of an API
Running command:
        * pytest -v -s --html=.\reports\report.html --self-contained-html test_get2_books.py
        * pytest test_put_books.py -v -s
        * pytest -m runget2 -v -s

"""
# ************ Importing Libraries ********** #
import logging
import pytest
from http_operation.get_book_by_random import Get2_Book

# ***************** program Starting ***********#
get_request = Get2_Book()
logger = logging.getLogger('Test Login')  # Logger


@pytest.mark.api
@pytest.mark.runget2
def test_get2_books_url(create_data):
    """ Calling get url method """
    try:
        get2_books_url = get_request.get_random_book()
        data_get = get2_books_url.as_dict
        logger.info(data_get)
        assert get2_books_url.status_code == 200
        logger.info("url validation passed")
        return get2_books_url
    except:
        logger.exception("Url entered is not valid")


@pytest.mark.api
@pytest.mark.runget2
def test_get2_book_header_verification():
    """Verifying the header of ge2 api  """
    try:
        response_headerverify = get_request.get2_books_header_validation()
        logger.info("Header validation is done")
        return response_headerverify
    except:
        logger.exception("Header of both response and request not match")


@pytest.mark.api
@pytest.mark.runget2
def test_get2_book_statuscode_verification():
    """ Verifying Status code for get1 book api"""
    try:
        status_response = get_request.get2_book_status_code_verification()
        logger.info("Status code verification done")
        return status_response
    except:
        logger.exception("Status code of the response is not valid")

# ************* End of the program *********** #
