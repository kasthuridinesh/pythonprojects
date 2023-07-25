"""
Author: Kasthuri
Description : Testing get2 function of an API
Running command:
        * pytest test_put_books.py -v -s
        * pytest -m runget2 -v -s

"""
# ************ Importing Libraries ********** #
import pytest

from Swagger_ui_api_automation.test.test_base import BaseTest
# ***************** program Starting ***********#


class TestBooksApi(BaseTest):

    @pytest.mark.allapi
    @pytest.mark.getbooks
    def test_get_book_verification(self):
        self.books_operation.verify_single_user_response()

    @pytest.mark.allapi
    @pytest.mark.getbooks
    def test_get_books_details_api(self):
        self.books_operation.get_book_detail_by_id()

    @pytest.mark.allapi
    @pytest.mark.getbooks
    def test_get_book_by_id_api(self):
        self.books_operation.get_book_detail_by_id()

    @pytest.mark.allapi
    @pytest.mark.createbook
    def test_create_book_api(self):
        self.books_operation.create_book()

    @pytest.mark.allapi
    @pytest.mark.updatebook
    def test_update_book_by_id_api(self):
        self.books_operation.update_book_details_by_id()

    @pytest.mark.allapi
    @pytest.mark.deletebook
    def test_delete_book_by_id_api(self):
        self.books_operation.delete_book_by_id()
#************* End of the program *********** #
