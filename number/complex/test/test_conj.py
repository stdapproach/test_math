import unittest

from py1 import Complex, isNearlyEqual

#books.txt - list of books with examples


class ConjTest(unittest.TestCase):
    def test_Alan_p13(self):
        z = Complex(1,2)
        actual = z.conj()
        self.assertEqual(actual, Complex(1, -2))
        actual2 = actual.conj()
        self.assertEqual(actual2, z)
        r, _ = z.polar()
        actual3 = z * actual
        self.assertTrue(isNearlyEqual(actual3.re(), r*r, 0.01))
        self.assertEqual((z+actual).re(), 2 * z.re())
        self.assertEqual((z - actual).im(), 2 * z.im())

    def test_Bird_p216(self):
        a = Complex(3,4)
        b = Complex.conj(a)
        self.assertEqual(a*b, 25)

    def test_Andreesku_p8(self):
        z1 = Complex(2,0)
        actual = z1.conj()
        self.assertEqual(actual.re(), z1.re())

    def test_Andreesku_p8_2(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        actual = z1.conj().conj()
        self.assertTrue(actual.nearly_eq(z1))

    def test_Andreesku_p8_3(self):
        z1 = Complex(1, 2)
        actual = z1 * z1.conj()
        self.assertTrue(actual.re() >= 0)

    def test_Andreesku_p8_3(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        actual = (z1+z2).conj()
        self.assertEqual(actual, z1.conj() + z2.conj())

    def test_Andreesku_p8_4(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, 4)
        actual = (z1*z2).conj()
        self.assertEqual(actual, z1.conj() * z2.conj())

    def test_Andreesku_p8_5(self):
        z1 = Complex(1, 2)
        actual = (Complex(1) / z1).conj()
        self.assertEqual(actual, Complex(1) / z1.conj())

    def test_Andreesku_p6(self):
        z = Complex(1, 2)
        actual1 = (z+z.conj())/2
        actual2 = (z - z.conj()) / (2 * Complex(0,1))
        self.assertEqual(actual1, z.re())
        self.assertEqual(actual2, z.im())

    def test_Brown_p16(self):
        z = Complex(2,-3)
        i = Complex(0,1)
        actual = (z.conj()+3*i).conj()
        self.assertEqual(actual, z - 3*i)

    def test_Zill_p5(self):
        z1 = Complex(2, 4)
        self.assertEqual(z1 - z1.conj(), 2 * Complex(0,1) * z1.im())


if __name__ == '__main__':
    unittest.main()
