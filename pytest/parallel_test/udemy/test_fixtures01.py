# fixtures are functions that are run by the pytest before the actual test functions
# eg= setup database connection, initialize webdriver
import pytest


# define fixtures function (parent method)
@pytest.fixture()
def setup_list():
    print("\n in fixtures..\n")
  #  city2 = ["new york", "london", "mumbai"]
    city = ["new york","london","mumbai"]
    return city


# getting data from setup_list function , inherits its properties
def test_getItem(setup_list):  # (child method1)
    print(setup_list[1:3])
    assert setup_list[0] == "new york"
    assert setup_list[::2] == ["new york", "mumbai"]
