import unittest
import inc_dec


def test_single_pytest():
    print("inc_dec hello and goodbye")
    assert inc_dec.increment(-1) == 2


class test_class_unittest_combo_file(unittest.TestCase):
    # This test class is not recognized by the discovery function and that is in line with what currently happens on our repo.

    def test_combo1_function_unittest(self):
        print("inc_dec hello")
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")

    def combo2_function_unittest(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")

    def inc_def_example(self):
        # This is not correctly named to be recognized as a test.
        self.assertEqual(inc_dec.increment(4), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()
