"""
Author: Kasthuri
Description : Testing delete function of an API
Running command:
        * pytest -v -s --html=.\reports\deletereport.html --self-contained-html test_delete_books.py
        * pytest test_put_books.py -v -s
        * pytest -m run_delete -v -s

"""
# ************ Importing Libraries ********** #
import pytest
from http_operation.delete_book_ import Delete_Book
import logging

# ***************** program Starting ***********#
delete_request = Delete_Book()
logger = logging.getLogger('Test Login')  # Logger


@pytest.mark.api
@pytest.mark.run_delete
def test_deleted_book_url(create_data):
    """ Calling delete book url method and printing url """
    try:
        deletebook_url = delete_request.delete_book_url()
        get_data = deletebook_url.as_dict
        assert deletebook_url.status_code == 200
        logger.info(get_data)
        logger.info("Delete book url verification done ")
    except:
        logger.exception(" Url verification failed ")


@pytest.mark.api
@pytest.mark.run_delete
def test_delete_book_byid():
    """ Calling delete book method and deleting book by id """
    try:
        response = delete_request.delete_particular_book()
        logger.info(response)
        logger.info("Deleted book successfully")
        return response
    except:
        logger.exception("Deleting book failed")


@pytest.mark.api
@pytest.mark.run_delete
def test_delete_statuscode_verification():
    """ Status code verification of delete api """
    try:
        status_response = delete_request.status_code_verification()
        logger.info("Status verification done ")
        return status_response
    except:
        logger.exception("Status verification failed")
# ************* End of the program *********** #
