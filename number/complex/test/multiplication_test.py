import unittest
import math
import cmath

import number.complex.py1 as py1
import number.complex.utils.complex_utils as cu

#//number/books.txt - list of books

class MultiplicationTest(unittest.TestCase):
    def test_square_i(self):
        #Given
        i = cu.mk_i()
        exp = -1
        #When
        act = i * i
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Bird_p255(self):
        #Given
        z1 = py1.mkComplexAlg(3, 2)
        z2 = py1.mkComplexAlg(4, -5)
        exp = py1.mkComplexAlg(22, -7)
        #When
        act = z1 * z2
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Bird_p255_2(self):
        #Given
        z1 = py1.mkComplexAlg(3, 4)
        z2 = py1.mkComplexAlg(3, -4)
        exp = 25
        #When
        act = z1 * z2
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Bird_p255_3(self):
        #Given
        z1 = py1.mkComplexAlg(1, -3)
        z2 = py1.mkComplexAlg(-2, 5)
        exp = py1.mkComplexAlg(13, 11)
        #When
        act = z1 * z2
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_bird_p255_4(self):
        #Given
        z1 = py1.mkComplexAlg(1, 1)
        exp1 = py1.mkComplexAlg(0, 2)
        exp2 = py1.mkComplexAlg(-4, 0)
        #When
        act1 = z1 * z1
        act2 = pow(z1, 4)
        #Then
        self.assertEqual(act1, exp1, "Should be equal")
        self.assertEqual(act2, exp2, "Should be equal")

    def test_Brown_p5(self):
        #Given
        z1 = py1.mkComplexAlg(2, -3)
        z2 = py1.mkComplexAlg(-2, 1)
        exp1 = py1.mkComplexAlg(-1, 8)
        #When
        act1 = z1 * z2
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Brown_p5_2(self):
        #Given
        z1 = py1.mkComplexAlg(3, 1)
        z2 = py1.mkComplexAlg(3, -1)
        z3 = py1.mkComplexAlg(1/5, 1/10)
        exp1 = py1.mkComplexAlg(2, 1)
        #When
        act1 = z1 * z2 * z3
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Brown_p5_3(self):
        #Given
        z = py1.mkComplexAlg(42, 43)
        z1 = 1 + z
        exp1 = 1 + 2 * z + z * z
        #When
        act1 = z1 * z1
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Brown_p5_4(self):
        #Given
        i = cu.mk_i()
        z1 = 1 + i
        z2 = 1 - i
        def f(z):
            return z*z-2*z+2

        exp1 = 0
        #When
        act1 = f(z1)
        act2 = f(z2)
        #Then
        self.assertEqual(act1, exp1, "Should be equal")
        self.assertEqual(act2, exp1, "Should be equal")

    def test_Brown_p8(self):
        #Given
        i = cu.mk_i()
        z1 = 1 - i
        exp1 = -4
        #When
        act1 = pow(z1, 4)
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Brown_p23(self):
        #Given
        i = cu.mk_i()
        z1 = i
        z2 = 1 - math.sqrt(3) * i
        z3 = math.sqrt(3)+i
        exp1 = 2 * (1+ math.sqrt(3) * i)
        #When
        act1 = z1 * z2 * z3
        #Then
        self.assertAlmostEqual(act1, exp1, 4, "Should be equal")

    def test_Jeffrey_p13(self):
        #Given
        i = cu.mk_i()
        exp1 = py1.mkComplexAlg(-15, -20)
        #When
        act1 = 5*i*(-4+3*i)
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Jeffrey_p13_2(self):
        #Given
        i = cu.mk_i()
        z1 = 3-2*i
        z2 = -1+4*i
        z3 = 1+i
        exp1 = py1.mkComplexAlg(-9, 19)
        #When
        act1 = z1*z2*z3
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Riley_p89(self):
        #Given
        i = cu.mk_i()
        exp1 = 1 + i
        #When
        act1 = i * (1-i)
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Taylor_p3(self):
        #Given
        i = cu.mk_i()
        z1 = 5+2*i
        z2 = 3-4*i
        exp1 = 23-14*i
        #When
        act1 = z1*z2
        #Then
        self.assertEqual(act1, exp1, "Should be equal")

    def test_Taylor_p20(self):
        #Given
        i = cu.mk_i()
        z1 = 2*cmath.exp(math.pi*i/3)
        z2 = 3*cmath.exp(2*math.pi*i/3)
        exp1 = -6
        #When
        act1 = z1*z2
        #Then
        self.assertAlmostEqual(act1, exp1, 2, "Should be equal")

    def test_Zill_p19(self):
        #Given
        i = cu.mk_i()
        z1 = -math.sqrt(3) - i
        exp1 = -8*i
        #When
        act1 = pow(z1, 3)
        #Then
        self.assertAlmostEqual(act1, exp1, 4, "Should be equal")

if __name__ == '__main__':
    unittest.main()
