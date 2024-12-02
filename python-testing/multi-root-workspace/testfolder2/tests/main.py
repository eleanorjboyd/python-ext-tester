import unittest

from test_math import TestMathMethods
from test_str import TestStringMethods

def suite():
    suite = unittest.TestSuite()

    for name in dir(TestMathMethods):
        if name.startswith('test_'):
            suite.addTest(TestMathMethods(name))

    for name in dir(TestStringMethods):
        if name.startswith('test_'):
            suite.addTest(TestStringMethods(name))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())