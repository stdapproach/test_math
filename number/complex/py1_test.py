import unittest

import py1

class SimplisticTest(unittest.TestCase):
    def test(self):
        actual = py1.foo()
        expected = 42
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

#bazel test //... --test_output=all --cache_test_results=no