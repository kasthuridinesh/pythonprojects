# ************** importing libraries *************
import pytest

from test.conftest import api_operations

# ***********************************************
""" using base test as fixture """


@pytest.mark.usefixtures("api_operations")
class BaseTest:
    pass
