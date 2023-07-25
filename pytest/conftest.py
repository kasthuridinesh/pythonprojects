""" Conftest helps us to access fixtures functions globally,
and it is accessed by multiple test files within a project"""

import pytest


@pytest.fixture
def input_value():
    input = 39
    return input
