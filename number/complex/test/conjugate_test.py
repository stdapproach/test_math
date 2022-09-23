import unittest

import number.complex.py1 as py1
import number.complex.utils.complex_utils as cu

#//number/books.txt - list of books

class ConjugateTest(unittest.TestCase):
    def test_Brown_p14(self):
        #Given
        z = py1.mkComplexAlg(1, 3)
        exp = py1.mkComplexAlg(1, -3)
        #When
        act = z.conjugate()
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Riley_p90(self):
        #Given
        i = cu.mk_i()
        a = 2
        b = 17
        z = a + 2 * i + 3 * i * b
        exp = a - i * (2 + 3 * b)
        #When
        act = z.conjugate()
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Conjugate2(self):
        #Given
        a = 2
        b = 17
        z0 = py1.mkComplexAlg(a, b)
        exp = py1.mkComplexAlg(a, b)
        #When
        act0 = z0.conjugate()
        act = act0.conjugate()
        #Then
        self.assertEqual(act, exp, "Should be equal")

    def test_Zill_p5(self):
        #Given
        z1 = py1.mkComplexAlg(6, 3)
        z2 = py1.mkComplexAlg(-5, -1)
        exp1 = py1.mkComplexAlg(6, -3)
        exp2 = py1.mkComplexAlg(-5, 1)
        #When
        act1 = z1.conjugate()
        act2 = z2.conjugate()
        #Then
        self.assertEqual(act1, exp1, "Should be equal")
        self.assertEqual(act2, exp2, "Should be equal")

if __name__ == '__main__':
    unittest.main()
