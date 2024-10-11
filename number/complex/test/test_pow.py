import math
import unittest
from math import sqrt, radians

from py1 import Complex, isNearlyEqual, isNearlyEqualByMod

#books.txt - list of books with examples

class PowTest(unittest.TestCase):
    def test_i(self):
        z = Complex(0,1)
        z1 = z.pow(2)
        self.assertTrue(z1.nearly_eq(-1))

    def test_pow0(self):
        z = Complex(0,1)
        z1 = z.pow(0)
        self.assertTrue(z1.nearly_eq(1))

    def test_pow1(self):
        z = Complex(0,1)
        z1 = z.pow(1)
        self.assertTrue(z1.nearly_eq(z))

    def test_Alan_p20(self):
        a = Complex(1, 1)
        actual = a.pow(25)
        expected = 4096 * Complex(1, 1)
        self.assertTrue(actual.nearly_eq(expected))

    def test_Bird_p225(self):
        z = Complex.from_polar((3, 20))
        z4 = z.pow(4)
        self.assertTrue(z4.nearly_eq(Complex.from_polar((81, 80))))

    def test_Bird_p225_2(self):
        z = Complex.from_polar((2, 35))
        z5 = z.pow(5)
        self.assertTrue(z5.nearly_eq(Complex.from_polar((32, 175))))

    def test_Bird_p225_3(self):
        z0 = Complex(-2, 3)
        r0, arg0 = z0.polar()
        self.assertEqual(r0, sqrt(13))
        self.assertTrue(isNearlyEqual(arg0, radians(123.69)))
        z = z0.pow(6)
        r, arg = z.polar()
        self.assertTrue(isNearlyEqual(r, 2197))
        self.assertTrue(isNearlyEqualByMod(arg, radians(742.14), radians(360)))
        exp6 = Complex.from_polar((2197, radians(22.14)))
        self.assertTrue(z.nearly_eq(exp6), 0.0001)

    def test_Bird_p225_4(self):
        z0 = Complex(-7, 5)
        r0, arg0 = z0.polar()
        self.assertEqual(r0, sqrt(74))
        self.assertTrue(isNearlyEqual(arg0, radians(144.46)))
        z = z0.pow(4)
        r, arg = z.polar()
        self.assertTrue(isNearlyEqual(r, 5476))
        self.assertTrue(isNearlyEqualByMod(arg, radians(217.84), radians(360)))
        exp4 = Complex(-4325, -3359)
        self.assertTrue(z.nearly_eq(exp4, 0.001))

    def test_Bird_p226(self):
        z0 = Complex.from_polar((1.5, radians(15)))
        z = z0.pow(5)
        expected = Complex.from_polar((7.59, radians(75)))
        self.assertTrue(z.nearly_eq(expected, 0.001))

    def test_Bird_p226_2(self):
        z0 = Complex(1, 2)
        z = z0.pow(6)
        expected = Complex.from_polar((125, radians(20.61)))
        self.assertTrue(z.nearly_eq(expected, 0.001))

    def test_Bird_p226_3(self):
        z0 = Complex.from_polar((3, radians(41)))
        actual = z0.pow(4)
        expected = Complex.from_polar((81, radians(164)))
        self.assertTrue(actual.nearly_eq(expected, 0.001))
        expCartesian = Complex(-77.86, 22.33)
        self.assertTrue(actual.nearly_eq(expCartesian))

    def test_Bird_p226_4(self):
        z0 = Complex(-2, -1)
        actual = z0.pow(5)
        expected = Complex.from_polar((55.90, radians(-47.18)))
        self.assertTrue(actual.nearly_eq(expected, 0.001))
        expCartesian = Complex(38, -41)
        self.assertTrue(actual.nearly_eq(expCartesian))

    def test_Andreesku_p5(self):
        z1 = Complex(1, 2)
        actual = z1.pow(2) * z1.pow(3)
        self.assertTrue(actual.nearly_eq(z1.pow(2+3)))

    def test_Andreesku_p5_2(self):
        z1 = Complex(1, 2)
        actual = z1.pow(2) / z1.pow(3)
        self.assertTrue(actual.nearly_eq(z1.pow(2-3)))

    def test_Andreesku_p5_3(self):
        z1 = Complex(1, 2)
        actual = (z1.pow(2)).pow(3)
        self.assertTrue(actual.nearly_eq(z1.pow(2*3)))

    def test_Andreesku_p5_4(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        actual = (z1 * z2).pow(3)
        self.assertTrue(actual.nearly_eq(z1.pow(3)*z2.pow(3)))

    def test_Andreesku_p5_5(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        z3 = Complex(2, 42)
        actual = z1 * (z2 + z3)
        self.assertTrue(actual.nearly_eq(z1 * z2 + z1 * z3))

    def test_Andreesku_p7(self):
        i = Complex(0, 1)
        self.assertEqual(i.pow(0), Complex(1,0))
        self.assertEqual(i.pow(1), Complex(0, 1))
        self.assertTrue(i.pow(2).nearly_eq(Complex(-1, 0)))
        self.assertTrue(i.pow(3).nearly_eq(-1 * Complex(0, 1)))
        self.assertTrue(i.pow(4).nearly_eq(Complex(1)))

    def test_Andreesku_p7_2(self):
        i = Complex(0, 1)
        actual = i.pow(105) + i.pow(23) + i.pow(20) - i.pow(34)
        self.assertTrue(actual.nearly_eq(Complex(2)))

    def test_Brown_p21(self):
        z = Complex(-1,1)
        actual = z.pow(7)
        self.assertTrue(actual.nearly_eq(Complex(-8) * Complex(1, 1)))

    def test_Taylor_p5(self):
        z1 = Complex(5, 2)
        actual = z1 * z1.pow(-1)
        self.assertTrue(actual.nearly_eq(Complex(1,0)))

    def test_Zill_p19(self):
        z1 = Complex(-math.sqrt(3), -1)
        actual = z1.pow(3)
        self.assertTrue(actual.nearly_eq(Complex(0,-8)))

    def test_Zill_p20(self):
        z1 = Complex(math.sqrt(3)/2, 1/2)
        actual = z1.pow(3)
        self.assertTrue(actual.nearly_eq(Complex(0,1)))



if __name__ == '__main__':
    unittest.main()