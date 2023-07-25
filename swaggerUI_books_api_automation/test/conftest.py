# ************ Importing Libraries ********** #
import pytest
from api_operations.books_operations import Books


# ***************** program Starting ***********#
@pytest.fixture(autouse=True, scope="class")
def api_operations(request):
    request.cls.books_operation = Books()


