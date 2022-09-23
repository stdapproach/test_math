import unittest

import number.complex.py1 as py1
import number.complex.utils.complex_utils as cu
import math

#//number/books.txt - list of books

class AddTest(unittest.TestCase):
    def test_Bird_p254(self):
        #Given
        z1 = py1.mkComplexAlg(2,3)
        z2 = py1.mkComplexAlg(3,-4)
        sum_expected = py1.mkComplexAlg(5,-1)
        diff_expected = py1.mkComplexAlg(-1,7)
        #Then
        self.assertEqual(z1 + z2, sum_expected, "Should be equal")
        self.assertEqual(z1 - z2, diff_expected, "Should be equal")

    def test_Brown_p4(self):
        #Given
        z1 = py1.mkComplexAlg(2,3)
        z2 = py1.mkComplexAlg(10,-1)
        sum_expected = z1
        negative_expected = py1.mkComplexAlg(-2,-3)
        #When
        z3 = z1 - z2
        z4 = z1 + (-z2)
        #Then
        self.assertEqual(z1 + 0, sum_expected, "Should be equal")
        self.assertEqual(z3, z4, "Should be equal")

    def test_Brown_p5(self):
        #Given
        i = cu.mk_i()
        act = (math.sqrt(2)-i) - i * (1-math.sqrt(2) * i)
        #When
        exp = -2 * i
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Jeffrey_p12(self):
        #Given
        z1 = py1.mkComplexAlg(3, 7)
        z2 = py1.mkComplexAlg(3, 2)
        sum_expected = py1.mkComplexAlg(6, 9)
        diff_expected = py1.mkComplexAlg(0, 5)
        #Then
        self.assertEqual(z1 + z2, sum_expected, "Should be equal")
        self.assertEqual(z1 - z2, diff_expected, "Should be equal")

    def test_Riley_p86(self):
        #Given
        z1 = py1.mkComplexAlg(1, 2)
        z2 = py1.mkComplexAlg(3, -4)
        z3 = py1.mkComplexAlg(-2, 1)
        exp = py1.mkComplexAlg(2, -1)
        #When
        act = z1 + z2 + z3
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Taylor_p8(self):
        #Given
        z1 = py1.mkComplexAlg(1, 2)
        z2 = py1.mkComplexAlg(3, -4)
        z3 = py1.mkComplexAlg(-2, 1)
        exp = py1.mkComplexAlg(2, -1)
        #When
        act = z1 + z2 + z3
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Urban_p401(self):
        #Given
        z1 = py1.mkComplexAlg(3, 1)
        z2 = py1.mkComplexAlg(1, -4)
        exp_sum = py1.mkComplexAlg(4, -3)
        exp_diff = py1.mkComplexAlg(2, 5)
        #When
        act_sum = z1 + z2
        act_diff = z1 - z2
        #Then
        self.assertEqual(act_sum, exp_sum, "Should be equal")
        self.assertEqual(act_diff, exp_diff, "Should be equal")

    def test_Urban_p402(self):
        #Given
        z1 = py1.mkComplexAlg(1, 2)
        z2 = py1.mkComplexAlg(3, -1)
        exp_1 = py1.mkComplexAlg(5, 3)
        exp_2 = py1.mkComplexAlg(-5, 4)
        #When
        act_sum = 2 * z1 + z2
        act_diff = z1 - 2 * z2
        #Then
        self.assertEqual(act_sum, exp_1, "Should be equal")
        self.assertEqual(act_diff, exp_2, "Should be equal")

if __name__ == '__main__':
    unittest.main()
