import pytest


@pytest.mark.parametrize("value", range(10))
def test_test(value):
    assert True
