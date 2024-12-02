import unittest
import inc_dec


class test_class_unittest(unittest.TestCase):
    def test1_function_unittest(self):
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")

    def test2_function_unittest(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")

    def inc_def_example(self):
        # This is not correctly named to be recognized as a test.
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()
