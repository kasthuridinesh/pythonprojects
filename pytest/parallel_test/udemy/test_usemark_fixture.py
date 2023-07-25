# using mark function in fixtures
import pytest

from parallel_test.udemy.test_fixtures01 import setup_list


# defining a decorator to  call the fixture function
# when we use mark function we can't access the setup_list inside fixtures function
@pytest.mark.xfail(reason="known issue: usefixtures cannot use the fixture's return")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert 1 == 1
    assert (setup_list[0])
