import unittest
import math
import cmath

import number.complex.py1 as py1
import number.complex.utils.complex_utils as cu

#//number/books.txt - list of books

class DivisionTest(unittest.TestCase):
    def test_Bird_p255(self):
        #Given
        i = cu.mk_i()
        z1 = 2-i*5
        z2 = 3+4*i
        exp = py1.mkComplexAlg(-14/25, -23/25)
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Brown_p7(self):
        #Given
        i = cu.mk_i()
        z1 = 4+i
        z2 = 2-3*i
        exp = py1.mkComplexAlg(5/13, 14/13)
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Jeffrey_p14(self):
        #Given
        i = cu.mk_i()
        z1 = 3+2*i
        z2 = 1+3*i
        exp = py1.mkComplexAlg(9/10, -7/10)
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Riley_p92(self):
        #Given
        i = cu.mk_i()
        z1 = 3-2*i
        z2 = -1+4*i
        exp = py1.mkComplexAlg(-11, -10) / 17
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Taylor_p7(self):
        #Given
        i = cu.mk_i()
        z1 = 1
        z2 = 2+3*i
        exp = py1.mkComplexAlg(2, -3) / 13
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Taylor_p20(self):
        #Given
        i = cu.mk_i()
        z1 = 2*cmath.exp(math.pi*i/3)
        z2 = 3*cmath.exp(2*math.pi*i/3)
        exp = (2/3)* cmath.exp(-math.pi*i/3)
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Zill_p6(self):
        #Given
        i = cu.mk_i()
        z1 = 2-3*i
        z2 = 4+6*i
        exp = py1.mkComplexAlg(-10, -24) / 52
        #When
        act = z1 / z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")

    def test_Zill_p6_2(self):
        #Given
        i = cu.mk_i()
        z1 = 1
        z2 = 2-3*i
        exp = py1.mkComplexAlg(2, 3) / 13
        #When
        act = z1 / z2
        act2 = act * z2
        #Then
        self.assertAlmostEqual(act, exp, 4, "Should be equal")
        self.assertEqual(act2, z1, "Should be equal")

if __name__ == '__main__':
    unittest.main()
