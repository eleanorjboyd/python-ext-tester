import inc_dec  # The code to test
import unittest


class ClassA(unittest.TestCase):
    def test_a1(self):
        print("test_inc hello")
        assert True

    def test_a2(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")

    def a3_not_found(self):
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")


class ClassB(unittest.TestCase):
    def test_b1(self):
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")

    def test_b2(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")

    def b3_not_found(self):
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()
