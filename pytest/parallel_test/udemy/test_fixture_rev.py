# using reverse string in fixture function to print list
import pytest
# importing user defined package and function
from test_fixtures01 import setup_list


# defining a my reverse method
def myReverse(setup_list):
    setup_list.reverse()
    return setup_list


# defining test method
def test_reverseList(setup_list):
    assert setup_list[::-1] == ["mumbai","london","new york"]
