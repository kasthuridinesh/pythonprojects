"""
Author: Kasthuri
Description : Testing get2 function of an API
Running command:
        * pytest test_put_books.py -v -s
        * pytest -m runget2 -v -s

"""
# ************ Importing Libraries ********** #
import pytest
from test.test_base import BaseTest
from utilities.logger import get_logger


# ***************** program Starting ***********#


class TestBooksApi(BaseTest):
    books_logger = get_logger()

    @pytest.mark.allapi
    @pytest.mark.getbooks
    def test_get_books_details_api(self):
        self.books_operation.verify_get_book_detail_by_id()
        self.books_logger.info("********** get books verification done for all the books **************")

    @pytest.mark.allapi
    @pytest.mark.getbooks_by_random
    def test_get_book_verification(self):
        self.books_operation.verify_book_by_random_id()
        self.books_logger.info("********** get book verification done**************")

    @pytest.mark.allapi
    @pytest.mark.getbooks
    def test_get_book_by_id_api(self):
        self.books_operation.verify_get_book_detail_by_id()
        self.books_logger.info("********** get book verification done by book id**************")

    @pytest.mark.allapi
    @pytest.mark.createbook
    def test_create_book_api(self):
        self.books_operation.verify_create_book()
        self.books_logger.info("********** create book verification done**************")

    @pytest.mark.allapi
    @pytest.mark.updatebook
    def test_update_book_by_id_api(self):
        self.books_operation.verify_update_book_details_by_id()
        self.books_logger.info("********** update book by id verification done**************")

    @pytest.mark.allapi
    @pytest.mark.deletebook
    def test_delete_book_by_id_api(self):
        self.books_operation.verify_delete_book_by_id()
        self.books_logger.info("********** delete book by id  verification done**************")

# ************* End of the program *********** #
