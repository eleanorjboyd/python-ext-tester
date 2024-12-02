import unittest
import time


class NumbersTest(unittest.TestCase):
    # def test_exception(self):
    #     raise Exception("Exception raised")
    #     # assert True

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        # time.sleep(1)
        for i in range(2000):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


class MyTest2(unittest.TestCase):
    def test_example2(self):
        for i in range(5):
            with self.subTest(msg=f"Iteration {i}"):
                self.assertTrue(i < 4)


class MyTest3(unittest.TestCase):
    def test_example3(self):
        for i, j in [(1, 2), (3, 4), (5, 6)]:
            with self.subTest(i=i, j=j):
                self.assertEqual(i + 1, j)


class MyTest4(unittest.TestCase):
    def test_example4(self):
        data = {"a": 1, "b": 2, "c": 3}
        for key, value in data.items():
            with self.subTest(key=key):
                self.assertTrue(value < 3)


class MyTest5(unittest.TestCase):
    def test_example5(self):
        tests = [
            {"name": "test1", "input": 5, "expected": 5},
            {"name": "test2", "input": 6, "expected": 7},
        ]

        for test in tests:
            with self.subTest(**test):
                self.assertEqual(test["input"], test["expected"])


class MyTest6(unittest.TestCase):
    def test_example6(self):
        tests = [
            {"name": "test1", "input": 5, "expected": 5},
            {"name": "test2", "input": 6, "expected": 7},
        ]

        for test in tests:
            with self.subTest(**test):
                self.assertEqual(test["input"], test["expected"])


class MyTest7(unittest.TestCase):
    def test_example7(self):
        tests = [(1, 2, "a"), (3, 4, "b"), (5, 6, "c")]

        for x, y, name in tests:
            with self.subTest(x=x, y=y, name=name):
                self.assertNotEqual(x, y)


class MyTest8(unittest.TestCase):
    def test_example9(self):
        input = ["stray&ampersand", "<unclosed tag", "[square]"]
        for x in input:
            with self.subTest(f"with: {x}"):
                self.assertEqual(x, "a")


class StringifySubTest(unittest.TestCase):
    def test_with_subtest_kwargs(self):
        data = ["stray&ampersand", "<unclosed tag", "[square]"]
        for item in data:
            with self.subTest(input=item):
                self.assertTrue(item < 5)
