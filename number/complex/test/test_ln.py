import math
import unittest
from math import radians

from py1 import Complex

from number.complex.py1 import isNearlyEqual


#books.txt - list of books with examples


class LnTest(unittest.TestCase):
    def test_ln_minus_i(self):
        z = Complex(0, -1)
        actual = z.Ln()
        self.assertEqual(actual, Complex(0, -math.pi/2))

    def test_Bird_p229(self):
        z = Complex.from_polar((4, 1.3))
        actual = z.Ln()
        expected = Complex(math.log(4), 1.3)
        self.assertEqual(actual, expected)
        self.assertTrue(actual.nearly_eq(Complex.from_polar((1.9, radians(43.17))), 0.001))

    def test_Bird_p229_2(self):
        z = 3 * Complex.exp(Complex(1, -1))
        actual = z.Ln()
        expected = Complex(2.0986, -1)
        self.assertTrue(actual.nearly_eq(expected))
        expected2 = Complex.from_polar((2.325, radians(-25.48)))
        self.assertTrue(actual.nearly_eq(expected2, 0.001))

    def test_Bird_p229_3(self):
        z = Complex(3, 4)
        actual = z.Ln()
        expected = Complex(math.log(5), 0.927)
        self.assertTrue(actual.nearly_eq(expected, 0.001))
        expected2 = Complex.from_polar((1.857, radians(29.95)))
        self.assertTrue(actual.nearly_eq(expected2, 0.001))

    def test_Bird_p229_4(self):
        z = Complex(5, 3)
        r, arg = z.polar()
        self.assertTrue(isNearlyEqual(r, 5.83, 0.001))
        self.assertTrue(isNearlyEqual(arg, 0.54, 0.001))

    def test_Bird_p229_5(self):
        z = Complex(-2.5, 4.2)
        r, arg = z.polar()
        self.assertTrue(isNearlyEqual(r, 4.89, 0.001))
        self.assertTrue(isNearlyEqual(arg, 2.11, 0.01))

    def test_Bird_p229_6(self):
        z = Complex.from_polar((3.6, 2))
        self.assertTrue(z.nearly_eq(Complex(-1.5, 3.27), 0.01))

    def test_Bird_p229_7(self):
        z = 2 * Complex.exp(Complex(3, math.pi/6))
        self.assertTrue(z.nearly_eq(Complex(34.79, 20.09), 0.01))

    def test_Bird_p229_8(self):
        z = 1.7 * Complex.exp(Complex(1.2, -2.5))
        self.assertTrue(z.nearly_eq(Complex(-4.52, -3.38), 0.01))

    def test_Bird_p229_9(self):
        z = 7 * Complex.exp(Complex(0, 2.1))
        actual = z.Ln()
        self.assertTrue(actual.nearly_eq(Complex(math.log(7), 2.1), 0.01))
        actual_polar = actual.polar()
        self.assertTrue(isNearlyEqual(actual_polar[0], 2.86))
        self.assertTrue(isNearlyEqual(actual_polar[1], radians(47.18)))

    def test_Bird_p229_10(self):
        z = Complex(2, 5)
        actual = z.Ln()
        expected = Complex.from_polar((2.06, radians(35.26)))
        self.assertTrue(actual.nearly_eq(expected, 0.001))

    def test_Taylor_p16(self):
        z = Complex(0, 1) * 2 * math.pi
        actual = Complex.exp(z)
        expected = Complex(1)
        self.assertTrue(actual.nearly_eq(expected))

    def test_Taylor_p16_2(self):
        z = Complex(0, 1) * math.pi
        actual = Complex.exp(z)
        expected = Complex(-1)
        self.assertTrue(actual.nearly_eq(expected))

    def test_Taylor_p16_3(self):
        z = Complex(0, 1) * math.pi / 2
        actual = Complex.exp(z)
        expected = Complex(0, 1)
        self.assertTrue(actual.nearly_eq(expected))

if __name__ == '__main__':
    unittest.main()