import math
import unittest

from py1 import Complex

#books.txt - list of books with examples


class MulTest(unittest.TestCase):
    def test_Alan_p13(self):
        a = Complex(0, 5)
        b = Complex(-4, 3)
        self.assertEqual(a * b, Complex(-15, -20))

    def test_Alan_p20(self):
        a = Complex(1, 1)
        b = Complex(math.sqrt(3), -1)
        actual = a * b
        expected = Complex.from_polar((2*math.sqrt(2), math.pi/12))
        self.assertTrue(actual.nearly_eq(expected))

    def test_Bird_p216(self):
        a = Complex(3, 2)
        b = Complex(4, -5)
        self.assertEqual(a * b, Complex(22, -7))

    def test_Bird_p216_2(self):
        a = Complex(1, -3)
        b = Complex(-2, 5)
        self.assertEqual(a * b, Complex(13, 11))

    def test_Bird_p216_3(self):
        z1 = Complex(1, -3)
        z2 = Complex(-2, 5)
        z3 = Complex(-3, -4)
        self.assertEqual(z1 * z2 * z3, Complex(5, -85))

    def test_Andreesku_p1(self):
        z1 = Complex(42, 0)
        z2 = Complex(43, 0)
        self.assertEqual((z1*z2).im(), 0)

    def test_Andreesku_p1_2(self):
        z1 = Complex(0, 42)
        z2 = Complex(0, 43)
        self.assertEqual((z1*z2).re(), -1*42*43)

    def test_Andreesku_p1_3(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        self.assertEqual(z1 * z2, Complex(7, 16))

    def test_Andreesku_p3(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        self.assertEqual(z1 * z2, z2 * z1)

    def test_Andreesku_p3_2(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        z3 = Complex(2, 42)
        self.assertEqual((z1 * z2) * z3, z1 * (z2 * z3))

    def test_Andreesku_p3_3(self):
        z1 = Complex(-5, 6)
        self.assertEqual(z1 * 1, z1)

    def test_Andreesku_p6(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        actual = z1 * z2
        self.assertEqual(actual.re(), z1.re()*z2.re() - z1.im()*z2.im())
        self.assertEqual(actual.im(), z1.im()*z2.re() + z2.im()*z1.re())

    def test_Brown_p4(self):
        z1 = Complex(2,-3)
        z2 = Complex(-2, 1)
        actual = z1 * z2
        self.assertEqual(actual, Complex(-1, 8))

    def test_Brown_p5(self):
        z = Complex(2,-3)
        i = Complex(0, 1)
        actual = i * z
        self.assertEqual(actual.re(), -z.im())
        self.assertEqual(actual.im(), z.re())

    def test_Brown_p5_2(self):
        z = Complex(2,-3)
        actual = (Complex(1) + z).pow(2)
        self.assertTrue(actual.nearly_eq(Complex(1) + 2*z + z*z))

    def test_Taylor_p3(self):
        z1 = Complex(5, 2)
        z2 = Complex(3, -4)
        self.assertEqual(z1 * z2, Complex(23, -14))

    def test_Taylor_p4(self):
        z1 = Complex(5, 2)
        self.assertEqual(z1 * Complex(1, 0), z1)

    def test_Taylor_p20(self):
        z1 = Complex.from_polar((2, math.pi/3))
        z2 = Complex.from_polar((3, 2 * math.pi / 3))
        actual = z1 * z2
        self.assertTrue(actual.nearly_eq(Complex(-6)))

    def test_Zill_p4(self):
        z1 = Complex(2, 4)
        z2 = Complex(-3, 8)
        self.assertEqual(z1 * z2, Complex(-38, 4))

    def test_Riley_p88(self):
        z1 = Complex(3, 2)
        z2 = Complex(-1, -4)
        self.assertEqual(z1 * z2, Complex(5, -14))



if __name__ == '__main__':
    unittest.main()
