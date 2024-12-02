import pytest


def test_numbers():
    pass


@pytest.mark.parametrize(("x"), [[0], [1], [10]])
def test_numbers2(x):
    pass


@pytest.mark.skip()
def test_numbers_skip(x):
    pass


def test_failing():
    assert 0


def test_one():
    pass

