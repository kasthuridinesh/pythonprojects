# ************** importing libraries *************
import pytest

# from test.conftest import api_operations


# ***********************************************
@pytest.mark.usefixtures("api_operations")
class BaseTest:
    pass

