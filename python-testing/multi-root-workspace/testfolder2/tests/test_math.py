import unittest


class TestMathMethods(unittest.TestCase):
    def test_numbers(self):
        pass

    def test_numbers2(self):
        for x in [[0], [1], [10]]:
            with self.subTest(x=x):
                pass

    @unittest.skip("demonstrating skipping")
    def test_numbers_skip(self):
        pass

    @unittest.expectedFailure
    def test_expected_failing(self):
        assert 0

    def test_failing(self):
        assert 0

    def test_one(self):
        pass

    def test_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
