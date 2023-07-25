# passing key value / 2 value passing  in the parameters and testing
# importing pytest for testing
import pytest


# define function to test the parameter
@pytest.mark.parametrize("inp,out", [(2, 4), (3, 27), (4, 256),(5, 35)])
def test_IO_checking(inp, out):
    assert (inp ** inp) == out
