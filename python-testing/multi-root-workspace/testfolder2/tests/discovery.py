import unittest
import inspect

loader = unittest.TestLoader()
suites = loader.discover("tests", pattern="test_*.py")


def get_sourceline(obj):
    s, n = inspect.getsourcelines(obj)
    for i, v in enumerate(s):
        if v.strip().startswith("def"):
            return str(n + i)
    return "*"


print("start")  # Don't remove this line
for suite in suites._tests:
    for cls in suite._tests:
        try:
            for m in cls._tests:
                tm = getattr(m, m._testMethodName)
                print(m.id() + ":" + get_sourceline(tm))
        except Exception as ex:
            pass
