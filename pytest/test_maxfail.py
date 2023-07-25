import pytest
import math


# Max fail is used to stop execution, when the defined number of test failed
# Here we give pytest --maxfail = 1, it will stop execution if 1 test get failed
def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 5


def test_square_failure():
    num = 7
    assert 7 * 7 == 40


def test_equality_failure():
    assert 10 == 11
