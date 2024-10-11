import math
import unittest

import numpy as np
from py1 import Complex, isNearlyEqual
from math import sqrt, radians

#books.txt - list of books with examples

class RootTest(unittest.TestCase):
    def test_1(self):
        z = Complex(41, 42)
        actual = z.root1(1)
        expected = z
        self.assertEqual(actual, expected)

    def test_root_1(self):
        z = Complex(41, 42)
        actual = z.root(1)
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], z)

    def test_2(self):
        z = Complex(-1)
        actual = z.root1(2)
        expected = Complex(0, 1)
        self.assertEqual(actual, expected)

    def test_root_2(self):
        z = Complex(-1)
        actual = z.root(2)
        expected = Complex(0, 1)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected))
        self.assertTrue(actual[1].nearly_eq(-1 * expected))

    def test_2_2(self):
        z = Complex(-9)
        actual = z.root1(2)
        expected = Complex(0, 3)
        self.assertEqual(actual, expected)

    def test_2_3(self):
        z = Complex(4)
        actual = z.root1(2)
        expected = Complex(2, 0)
        self.assertEqual(actual, expected)

    def test_Bird_p226(self):
        z = Complex(5, 12)
        actual = z.root1(2)
        expected = Complex.from_polar((sqrt(13), radians(33.69)))
        self.assertTrue(actual.nearly_eq(expected))

    def test_Bird_p226_2(self):
        z = Complex(5, 12)
        self.assertTrue(z.nearly_eq(Complex.from_polar((13, radians(67.38)))))
        actual = z.root(2)
        expected1 = Complex.from_polar((sqrt(13), radians(33.69)))
        expected2 = Complex.from_polar((sqrt(13), radians(213.69)))
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1))
        self.assertTrue(actual[1].nearly_eq(expected2))

    def test_Bird_p227(self):
        z = Complex(5, 3)
        self.assertTrue(z.nearly_eq(Complex.from_polar((sqrt(34), radians(30.96)))))
        actual = z.root(2)
        expected1 = Complex.from_polar((2.415, radians(15.48)))
        expected2 = Complex.from_polar((2.415, radians(195.48)))
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_2(self):
        z = Complex(-14, 3)
        a = -2
        b = 5
        self.assertTrue(z.nearly_eq(Complex.from_polar((sqrt(205), radians(167.905)))))
        #actual0 = z.
        actual = z.pow_ratio(a,b)
        self.assertEqual(len(actual), 5)
        exp_r = 0.3449
        exp_arg0 = radians(-67.164)
        expected1 = Complex.from_polar((exp_r, exp_arg0 + radians(360/5)))
        expected2 = Complex.from_polar((exp_r, exp_arg0 + 2 * radians(360 / 5)))
        expected3 = Complex.from_polar((exp_r, exp_arg0 + 3 * radians(360 / 5)))
        expected4 = Complex.from_polar((exp_r, exp_arg0 + 4 * radians(360 / 5)))
        expected5 = Complex.from_polar((exp_r, exp_arg0 + 5 * radians(360 / 5)))
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))
        self.assertTrue(actual[2].nearly_eq(expected3, 0.001))
        self.assertTrue(actual[3].nearly_eq(expected4, 0.001))
        self.assertTrue(actual[4].nearly_eq(expected5, 0.001))

    def test_Bird_p227_3(self):
        z = Complex(1, 1)
        actual = z.root(2)
        expected1 = Complex(1.099, 0.455)
        expected2 = Complex(-1.099, -0.455)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_4(self):
        z = Complex(0, 1)
        actual = z.root(2)
        expected1 = Complex(0.707, 0.707)
        expected2 = Complex(-0.707, -0.707)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_5(self):
        z = Complex(3, -4)
        actual = z.root(2)
        expected1 = Complex(2, -1)
        expected2 = Complex(-2, 1)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_6(self):
        z = Complex(-1, -2)
        actual = z.root(2)
        expected1 = Complex(0.786, -1.272)
        expected2 = Complex(-0.786, 1.272)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_7(self):
        z = Complex.from_polar((7, radians(60)))
        actual = z.root(2)
        expected1 = Complex(2.291, 1.323)
        expected2 = Complex(-2.291, -1.323)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_8(self):
        z = Complex.from_polar((12, math.pi*3/2))
        actual = z.root(2)
        expected2 = Complex(-2.449, 2.449)
        expected1 = Complex(2.449, -2.449)
        self.assertEqual(len(actual), 2)
        self.assertTrue(actual[0].nearly_eq(expected1, 0.001))
        self.assertTrue(actual[1].nearly_eq(expected2, 0.001))

    def test_Bird_p227_9(self):
        z = Complex(3, 4)
        actual = z.root(3)
        expected_r = 1.71
        list_r = []
        list_arg = []
        for it in actual:
            r, arg = it.polar()
            list_r.append(r)
            list_arg.append(arg)

        self.assertEqual(len(actual), 3)
        self.assertTrue(np.allclose(list_r, list_r[0]))
        self.assertTrue(isNearlyEqual(list_r[0], expected_r), 0.001)

        self.assertTrue(isNearlyEqual(list_arg[0], radians(17.71)))
        self.assertTrue(isNearlyEqual(list_arg[1], radians(137.71)))
        self.assertTrue(isNearlyEqual(list_arg[2], radians(257.71-360)))

    def test_Bird_p229(self):
        z = Complex.from_polar((7.2, 1.5))
        expected = Complex(0.509, 7.182)
        self.assertTrue(z.nearly_eq(expected))

    def test_Alan_p24(self):
        w = Complex(1,1)
        w_r, w_arg = w.polar()
        self.assertEqual(w_r, math.sqrt(2))
        self.assertEqual(w_arg, math.pi/4)
        actual = w.root1(3)
        act_r, act_arg = actual.polar()
        self.assertEqual(act_r, math.pow(2, 1/6))
        self.assertEqual(act_arg, math.pi/12)

    def test_Alan_p24_cont(self):
        w = Complex(1,1)
        actual = w.root(3)
        self.assertEqual(len(actual), 3)
        expected = []
        r = math.pow(2, 1/6)
        for i in range(0, 3):
            arg = (1/12)*(1+8*i)*math.pi
            expected.append(Complex.from_polar((r, arg)))

        for i in range(0, 3):
            self.assertEqual(actual[i], expected[i], f"for i={i}")

    def test_Alan_p25(self):
        w = Complex(1, 1)
        actual = w.root(2)
        self.assertEqual(len(actual), 2)
        r2 = math.sqrt(2)
        self.assertTrue(actual[0].nearly_eq(Complex(math.sqrt((r2+1)/2), math.sqrt((r2-1)/2))))
        self.assertTrue(actual[1].nearly_eq(Complex(-math.sqrt((r2 + 1) / 2), -math.sqrt((r2 - 1) / 2))))

    def test_Brown_p28(self):
        z = Complex(-16)
        actual = z.root1(4)
        expected = Complex.from_polar((2, math.pi/4))
        self.assertTrue(actual.nearly_eq(expected))

    def test_Brown_p28_cont(self):
        z = Complex(-16)
        actual = z.root(4)
        self.assertEqual(len(actual), 4)
        r = math.sqrt(2)
        c0 = Complex(1,1) * r
        c1 = r * Complex(-1, 1)
        c2 = r * Complex(-1, -1)
        c3 = r * Complex(1, -1)
        self.assertTrue(actual[0].nearly_eq(c0))
        self.assertTrue(actual[1].nearly_eq(c1))
        self.assertTrue(actual[2].nearly_eq(c2))
        self.assertTrue(actual[3].nearly_eq(c3))

    def test_Zill_p24(self):
        z = Complex(0, 1)
        actual = z.root1(3)
        expected = Complex.from_polar((1, math.pi/6))
        self.assertTrue(actual.nearly_eq(expected))

    def test_Wunsch_p11(self):
        z = Complex(-9, 0)
        actual = z.root1(2)
        expected = Complex(0, 3)
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()