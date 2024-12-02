import unittest

class TestStringMethods(unittest.TestCase):

    def test_str(self):
        pass

    def test_str2(self):
        for x in [["hello"], ["s p a c e"], ["ಅನು ಕಾರ್ತಿಕ್"]]:
            with self.subTest(x=x):
                pass


    @unittest.skip("demonstrating skipping")
    def test_str_skip(self):
        pass


    def test_another_test(self):
        pass

    @unittest.expectedFailure
    def test_expect_fail(self):
        assert 0

if __name__ == '__main__':
    unittest.main()