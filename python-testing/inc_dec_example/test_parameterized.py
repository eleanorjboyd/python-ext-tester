import pytest

import os
import sys

print("HERE", sys.path)
print(os.getcwd())


class TestMethods:
    class TestNestedAgain:
        # class TestABC:

        # Testing pytest with parametrized tests. The first two pass, the third fails.
        # The tests ids are parametrize_tests.py::test_adding[3+5-8] and so on.
        @pytest.mark.parametrize(
            "actual, expected",
            [("3+3", 5), ("2+3+4", 6), ("6+9", 16)],
            ids=["test adding", "2      +V", "\n ffda"],
        )
        def test_adding(self, actual, expected):
            print("Pytest version:", pytest.__version__)
            print("HERE", sys.path)
            print(os.getcwd())
            assert eval(actual) == expected

    @pytest.mark.parametrize("num", range(1, 200))
    def test_odd_even(self, num):
        print("dsafjkdals;gdksa;tjeoiwraphgvnajdskflshewapirfhguvpisdahbfleri")
        assert num % 2 == 0


if __name__ == "__main__":
    pytest.main()
