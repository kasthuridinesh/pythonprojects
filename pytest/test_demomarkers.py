# using markers function to test the greatest number
"""Markers are used   to run only a specific set of tests. Markers are used to set various features/attributes to
test functions. Pytest provides many inbuilt markers such as xfail, skip and parametrize.

"""

import pytest


# using markers function to execute particular test
# test method with using mark function
@pytest.mark.great
def test_great():
    num = 25
    assert num == 5


# test function without using mark function
def test_great_equal():
    num = 30
    assert num >= 2


# to test  the great functions only -- (pytest -m great<function name> -v)

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
