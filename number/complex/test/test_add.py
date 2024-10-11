import unittest

from py1 import Complex

#books.txt - list of books with examples


class AddTest(unittest.TestCase):
    def test_Bird_p215(self):
        a = Complex(2, 3)
        b = Complex(3, -4)
        self.assertEqual(a+b, Complex(5,-1))

    def test_Bird_p215_2(self):
        a = Complex(2, 3)
        b = Complex(3, -4)
        self.assertEqual(a-b, Complex(-1,7))

    def test_Alan_p12(self):
        z1 = Complex(3, 7)
        z2 = Complex(3, 2)
        self.assertEqual(z1 + z2, Complex(6, 9))
        self.assertEqual(z1 - z2, Complex(0, 5))

    def test_Andreesku_p1(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        self.assertEqual(z1 + z2, Complex(-4, 4))

    def test_Andreesku_p1_2(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        self.assertEqual(z1 + z2, z2 + z1)

    def test_Andreesku_p1_3(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        z3 = Complex(2, 42)
        self.assertEqual((z1 + z2) + z3, z1 + (z2 + z3))

    def test_Andreesku_p1_4(self):
        z1 = Complex(-5, 6)
        self.assertEqual(z1 + 0, z1)

    def test_Andreesku_p1_5(self):
        z1 = Complex(-5, 6)
        self.assertEqual(z1 + (-1*z1), Complex(0,0))

    def test_Andreesku_p6(self):
        z1 = Complex(-5, 6)
        z2 = Complex(1, -2)
        self.assertEqual((z1 + z2).re(), z1.re() + z2.re())
        self.assertEqual((z1 + z2).im(), z1.im() + z2.im())

    def test_Taylor_p3(self):
        z1 = Complex(5, 2)
        z2 = Complex(3, -4)
        self.assertEqual(z1 + z2, Complex(8, -2))

    def test_Taylor_p4(self):
        z1 = Complex(5, 2)
        self.assertEqual(z1 + Complex(0, 0), z1)

    def test_Taylor_p4_2(self):
        z1 = Complex(5, 2)
        self.assertEqual(z1 - z1, Complex(0,0))

    def test_Zill_p4(self):
        z1 = Complex(2, 4)
        z2 = Complex(-3, 8)
        self.assertEqual(z1 + z2, Complex(-1, 12))

    def test_Riley_p86(self):
        z1 = Complex(1, 2)
        z2 = Complex(3, -4)
        z3 = Complex(-2, 1)
        self.assertEqual(z1 + z2 + z3, Complex(2, -1))

if __name__ == '__main__':
    unittest.main()
