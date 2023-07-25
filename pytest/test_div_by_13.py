# This test_div_by_13 function which aquires the property from confest
import pytest


# input_value is the fixtures function,and it defined as conftest. it is accessed by test_divisible_13

def test_divisible_by_13(input_value):
    assert input_value % 13 == 0


def test_divisible_by_12(input_value):
    assert input_value % 12 == 0
