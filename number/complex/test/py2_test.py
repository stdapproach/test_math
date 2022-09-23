import unittest

import number.complex.py1 as py1

class SimplisticTest2(unittest.TestCase):
    def test(self):
        actual = py1.foo()
        expected = 42
        self.assertEqual(actual, expected)

    def testEquality(self):
        z1 = py1.mkComplexAlg(42,43)
        z2 = py1.mkComplexAlg(42,43)
        z3 = py1.mkComplexAlg(2,1)
        self.assertEqual(z1, z2, "Should be equal")
        self.assertNotEqual(z1, z3, "Should NOT be equal")

if __name__ == '__main__':
    unittest.main()

#bazel test //... --test_output=all --cache_test_results=no
#self.assertTrue("adp::FooTopic" in s.keys())