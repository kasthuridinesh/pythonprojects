# ************ Importing Libraries ********** #
import pytest

from Swagger_ui_api_automation.api_operations.books_operations import Books


# from api_operations.books_operations import Books


# ***************** program Starting ***********#
@pytest.fixture(autouse=True, scope="class")
def api_operations(request):
    request.cls.books_operation = Books()


