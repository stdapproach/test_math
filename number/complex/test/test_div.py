import math
import unittest

from py1 import Complex

#books.txt - list of books with examples


class ConjTest(unittest.TestCase):
    def test_Alan_p14(self):
        z1 = Complex(3, 2)
        z2 = Complex(1, 3)
        self.assertEqual(z1/z2, Complex(9/10, -7/10))

    def test_Alan_p20(self):
        a = Complex(1, 1)
        b = Complex(math.sqrt(3), -1)
        actual = a / b
        expected = Complex.from_polar((1/math.sqrt(2), 5*math.pi/12))
        self.assertTrue(actual.nearly_eq(expected))

    def test_Bird_p216(self):
        a = Complex(2,-5)
        b = Complex(3,4)
        self.assertEqual(a/b, Complex(-14/25,-23/25))

    def test_Bird_p216_2(self):
        a = Complex(1, -3)
        b = Complex(-3, -4)
        self.assertEqual(a / b, Complex(9/25, 13/25))

    def test_Bird_p216_3(self):
        a = Complex(1, -3)
        b = Complex(-2, 5)
        self.assertEqual(a * b / (a + b), Complex(9/5, -37/5))

    def test_Andreesku_p3(self):
        z1 = Complex(-5, 6)
        self.assertEqual(z1 / z1, Complex(1,0))

    def test_Andreesku_p4(self):
        z1 = Complex(1, 2)
        self.assertEqual(Complex(1) / z1, Complex(1/5, -2/5))

    def test_Andreesku_p4_2(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        self.assertEqual(z1/z2, Complex(11/25, 2/25))

    def test_Taylor_p7(self):
        z = Complex(3, 4)
        actual = Complex(1) / z
        expected = z.conj() / (z * z.conj())
        self.assertEqual(actual ,expected)

    def test_Taylor_p7_2(self):
        z = Complex(2, 3)
        actual = Complex(1) / z
        expected = Complex(2/13, -3/13)
        self.assertEqual(actual ,expected)

    def test_Taylor_p7_3(self):
        z1 = Complex(3, 4)
        z2 = Complex(3, -4)
        actual = z1 / z2
        expected = Complex(-7/25, 24/25)
        self.assertEqual(actual ,expected)

    def test_Taylor_p20(self):
        z1 = Complex.from_polar((2, math.pi/3))
        z2 = Complex.from_polar((3, 2 * math.pi / 3))
        actual = z1 / z2
        self.assertTrue(actual.nearly_eq(Complex(1/3, -math.sqrt(3)/3)))

    def test_Zill_p5(self):
        z1 = Complex(2, -3)
        z2 = Complex(4, 6)
        self.assertEqual(z1 / z2, Complex(-10, -24)/52)

    def test_Zill_p6(self):
        z1 = Complex(2, -3)
        self.assertEqual(Complex(1, 0) / z1, Complex(2/13, 3/13))

    def test_riley_p92(self):
        z1 = Complex(3, -2)
        z2 = Complex(-1, 4)
        self.assertEqual(z1 / z2, Complex(-11/17, -10/17))


if __name__ == '__main__':
    unittest.main()
