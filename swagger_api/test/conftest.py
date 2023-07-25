# ************ Importing Libraries ********** #
import pytest
from utils.post_parser import read_file
from utils.put_parser import read
from global_dir.directory_config import PUT_JSON, POST_JSON


@pytest.fixture(scope='session')
def create_data():
    payload = read_file(POST_JSON)
    yield payload


@pytest.fixture(scope='session')
def create_put():
    payload = read(PUT_JSON)
    yield payload

# ************* End of the program *********** #
