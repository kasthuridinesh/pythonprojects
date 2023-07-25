#

import pytest
import yaml
from _pytest.fixtures import fixture


@pytest.fixture(scope='session')
def start_exec():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yield data
    print("quit")