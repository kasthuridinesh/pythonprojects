import pytest

'''
Fixtures: Fixtures are used to feed some data to test such as database connection, URLs to 
test and some sort of input data.
instead of running the same code for every test, we can attach fixtures function. it will run and return test before 
executing each test. 

'''


@pytest.fixture
def input_value():  # input_value is consider as a fixture function.It is inherited by the functions
    # test_divisible_by_3 and test_divisible_by_6
    input = 39
    return input


# input value is inherit from the input_value fixtures function and checking that the value is divisible by 3 or not
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


# input value is inherit from the input_value fixtures function and checking that the value is divisible by 6 or not
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
