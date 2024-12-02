import pytest


def test_str():
    pass


@pytest.mark.parametrize(("x"), [["hello"], ["s p a c e"], ["ಅನು ಕಾರ್ತಿಕ್"]])
def test_str2(x):
    pass


@pytest.mark.skip()
def test_str_skip(x):
    pass


def test_another_test():
    pass
