import math
import unittest
from math import sqrt, radians

from py1 import Complex, isNearlyEqual

#books.txt - list of books with examples

class PolarTest(unittest.TestCase):
    def test_i(self):
        z = Complex(0,1)
        r, arg = Complex.polar(z)
        self.assertEqual(r, 1)
        self.assertTrue(isNearlyEqual(arg, radians(90)))
        pass

    def test_Bird_p219(self):
        z = Complex(2,3)
        r, arg = Complex.polar(z)
        self.assertEqual(r, sqrt(13))
        self.assertTrue(isNearlyEqual(arg, radians(56.31)))
        pass

    def test_Bird_p219_2(self):
        z1 = Complex(3,4)
        z2 = Complex(-3, 4)
        r1, arg1 = Complex.polar(z1)
        self.assertEqual(r1, sqrt(25))
        self.assertTrue(isNearlyEqual(arg1, radians(53.13)))
        r2, arg2 = Complex.polar(z2)
        self.assertEqual(r1, r2)
        self.assertTrue(isNearlyEqual(arg2, radians(180)-arg1))
        pass

    def test_Bird_p219_3(self):
        z = Complex(-3,4)
        r, arg = Complex.polar(z)
        self.assertEqual(r, sqrt(25))
        self.assertTrue(isNearlyEqual(arg, radians(126.87)))
        pass

    def test_Bird_p220(self):
        r = 4
        ang = radians(30)
        z = Complex.from_polar((r, ang))
        self.assertTrue(Complex.nearly_eq(z, Complex(3.464, 2), 0.001))

    def test_Bird_p220_2(self):
        r = 7
        ang = radians(-145)
        z = Complex.from_polar((r, ang))
        self.assertTrue(Complex.nearly_eq(z, Complex(-5.734, -4.015)))

    def test_Bird_p220_3(self):
        z1 = Complex.from_polar((8, radians(25)))
        z2 = Complex.from_polar((4, radians(60)))
        self.assertTrue(Complex.nearly_eq(z1 * z2, Complex.from_polar((32, radians(85)))))

    def test_Bird_p220_4(self):
        z1 = Complex.from_polar((3, radians(16)))
        z2 = Complex.from_polar((5, radians(-44)))
        z3 = Complex.from_polar((2, radians(80)))
        self.assertTrue(Complex.nearly_eq(z1 * z2 * z3, Complex.from_polar((30, radians(52)))))

    def test_Bird_p220_5(self):
        z1 = Complex.from_polar((16, radians(75)))
        z2 = Complex.from_polar((2, radians(15)))
        self.assertTrue(Complex.nearly_eq(z1 / z2, Complex.from_polar((8, radians(60)))))

    def test_Bird_p220_6(self):
        z1 = Complex.from_polar((2, radians(30))) #2 cos(30) + 2 i sin(30)
        z2 = Complex.from_polar((5, radians(-45))) #5 cos(45) - 5 i sin(45)
        z3 = Complex.from_polar((4, radians(120))) #4 cos(120) + 4 i sin(120)
        z = z1 + z2 - z3
        expected = Complex(2+5/sqrt(2) + sqrt(3), 1-5/sqrt(2)-2*sqrt(3))
        exp_r = sqrt(5*(9+sqrt(2)+3*sqrt(6))) # 9.421
        # this book has a quite error: and propose r=9.425 as answer, where the proper value is 9.421
        self.assertTrue(isNearlyEqual(exp_r, 9.421, 0.001))
        self.assertTrue(Complex.nearly_eq(z, expected))
        self.assertTrue(Complex.nearly_eq(z, Complex.from_polar((exp_r, radians(-39.54))), 0.001))

    def test_Bird_p221(self):
        i = Complex(0, 1)
        z = i*i*i*(Complex(1)-i)
        self.assertTrue(Complex.nearly_eq(z, Complex.from_polar((sqrt(2), radians(-135)))))

    def test_Bird_p221_2(self):
        z = Complex.from_polar((3.5, radians(-120)))
        self.assertTrue(Complex.nearly_eq(z, Complex(-1.75, -3.031)))

    def test_Wunsch_p6(self):
        z1 = Complex(-math.sqrt(3), -1)
        r, arg = z1.polar()
        self.assertEqual(r, 2)
        self.assertTrue(isNearlyEqual(arg, -2.618, 0.001))


if __name__ == '__main__':
    unittest.main()