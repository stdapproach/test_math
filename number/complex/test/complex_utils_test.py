from cmath import isfinite, isinf, isnan
import unittest

import number.complex.utils.complex_utils as cu

class SimplisticTest(unittest.TestCase):
    def test0(self):
        self.assertEqual(42, 42)

    def test_Nan_float(self):
        def isThing(val):
            return isnan(val)
        def mkThing():
            return cu.mknan_float()

        z0 = float('NaN')

        z1 = mkThing()
        self.assertTrue(isThing(z1), "Should be NaN")
        self.assertFalse(isfinite(z1), "Should be non Finite")
        
        self.assertNotEqual(z1, z0, "Should be NOT equal two Nan")
        self.assertNotEqual(42, z1, "Should be NOT equal two Nan")
        z3 = z0-z1
        self.assertTrue(isThing(z3), "Should be NaN")
        z4 = z0-42
        self.assertTrue(isThing(z4), "Should be NaN")
        z5 = z0/z1
        self.assertTrue(isThing(z5), "Should be NaN")

    def test_Inf_float(self):
        def isThing(val):
            return isinf(val)
        def mkThing():
            return cu.mkinf_float()

        z0 = float('Inf')

        z1 = mkThing()
        self.assertTrue(isThing(z1), "Should be Inf")
        self.assertFalse(isfinite(z1), "Should be non Finite")
        
        self.assertEqual(z1, z0, "Should be equal two Inf")
        self.assertNotEqual(42, z1, "Should be NOT equal two Inf")
        z3 = z0-z1
        self.assertFalse(isThing(z3), "Should be NOT Inf")
        z4 = z0-42
        self.assertTrue(isThing(z4), "Should be Inf")
        z5 = z0/z1
        self.assertFalse(isThing(z5), "Should be NOT Inf")

if __name__ == '__main__':
    unittest.main()
