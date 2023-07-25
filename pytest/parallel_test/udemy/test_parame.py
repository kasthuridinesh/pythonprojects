# parametrize testing is used to create for passing multiple values

import pytest


@pytest.mark.parametrize('test_input', [82, 78, 45, 66])
def test_parame01(test_input):
    assert test_input > 50
