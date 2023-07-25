import pytest


# xfail and skip are used to test  relevant test,
# xfail = will execute the xfail test but not considered as failed test.
# skip test is used to skip particular test will not execute the test.


@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
