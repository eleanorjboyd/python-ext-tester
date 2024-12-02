import pytest
import time


@pytest.mark.parametrize("num", range(1, 30))
def test_param_other(num):
    time.sleep(0.2)
    assert True
