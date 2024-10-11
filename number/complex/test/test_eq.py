import math
import unittest

from py1 import Complex, isNearlyEqual


#books.txt - list of books with examples


class EqTest(unittest.TestCase):
    def test_is_None(self):
        val = Complex(0,42)
        self.assertFalse(val.is_none(), "Expected regular complex value:  no None value")
        # it's hard to create math.complex with None values

    def test_i_square(self):
        val = Complex(0, 1)
        act = val * val
        self.assertEqual(act, -1)

    def test_i_square_1(self):
        val = Complex(0, 1)
        act = val * val + 1
        self.assertEqual(act, 0)

    def test_i_square_2(self):
        val = Complex(0, 1)
        act = val * val
        act *= act
        self.assertEqual(act, 1)

    def test_real_square(self):
        val = Complex(2, 0)
        act = val * val
        self.assertEqual(act, 4)

    def test_alan_p11(self):
        z = Complex(3, -7)
        self.assertEqual(z.re(), 3)
        self.assertEqual(z.im(), -7)

    def test_alan_p14(self):
        z = Complex(1, 2)
        r, _ = z.polar()
        a = z
        b = a.conj()
        c = a*b
        d = c.root1(2)
        actual_r, _ = d.polar()
        self.assertEqual(r, actual_r)

    def test_Bird_p213(self):
        val1 = Complex(-1, 2)
        val2 = Complex(-1, -2)

        def polynome(z: Complex):
            return z * z + 2 * z + 5

        self.assertEqual(polynome(val1), 0)
        self.assertEqual(polynome(val2), 0)

    def test_Bird_p213_problem1(self):
        val1 = Complex(0, 2)
        val2 = Complex(0, -2)

        def polynome(z: Complex):
            return z * z + 4

        self.assertEqual(polynome(val1), 0)
        self.assertEqual(polynome(val2), 0)

    def test_Bird_p213_problem2(self):
        val1 = Complex(-3/4, math.sqrt(31)/4)
        val2 = Complex(-3/4, -math.sqrt(31)/4)

        def polynome(z: Complex):
            return 2 * z * z + 3 * z + 5

        self.assertEqual(polynome(val1), 0)
        self.assertEqual(polynome(val2), 0)

    def test_Andreesku_p10(self):
        z = Complex(4, 3)
        r, _ = z.polar()
        self.assertEqual(r, math.sqrt(25))

    def test_Andreesku_p10_2(self):
        z = Complex(4, 3)
        r, _ = z.polar()
        self.assertTrue(-r <= z.re())
        self.assertTrue(z.re() <= r)
        self.assertTrue(-r <= z.im())
        self.assertTrue(z.im() <= r)

    def test_Andreesku_p10_3(self):
        z1 = Complex(4, 3)
        r1, _ = z1.polar()
        z2 = -1 * z1
        r2, _ = z2.polar()
        z3 = z1.conj()
        r3, _ = z3.polar()
        self.assertTrue(r1 == r2)
        self.assertTrue(r1 == r3)
        self.assertTrue(r2 == r3)

    def test_Andreesku_p10_4(self):
        z = Complex(1, 2)
        actual = z * z.conj()
        r, _ = z.polar()
        self.assertTrue(actual.nearly_eq(Complex(r*r)))

    def test_Brown_p16(self):
        z = Complex(2,-3)
        i = Complex(0,1)
        actual = (z.conj() - i).re()
        self.assertEqual(actual, 2)

    def test_Brown_p18(self):
        z = Complex(-1,-1)
        r, arg = z.polar()
        self.assertEqual(r, math.sqrt(2))
        self.assertEqual(arg, -3*math.pi/4)

    def test_Brown_p20(self):
        z1 = Complex(2,3)
        z2 = Complex(1,4)
        z = z1 * z2
        r1, arg1 = z1.polar()
        r2, arg2 = z2.polar()
        actual_r, actual_arg = z.polar()
        self.assertTrue(isNearlyEqual(actual_r, r1 * r2))

    def test_Taylor_p19(self):
        z = Complex(2,2)
        r, arg = z.polar()
        self.assertEqual(r, 2 * math.sqrt(2))
        self.assertEqual(arg, math.pi/4)

    def test_Taylor_p19_2(self):
        z = Complex.from_polar((2, math.pi/6))
        self.assertTrue(z.nearly_eq(Complex(math.sqrt(3), 1)))

    def test_Zill_p17(self):
        z = Complex(-math.sqrt(3), -1)
        self.assertTrue(z.nearly_eq(Complex.from_polar((2, 7*math.pi/6))))

    def test_Riley_p87(self):
        z = Complex(2, -3)
        r, _ = z.polar()
        self.assertEqual(r, math.sqrt(13))

    def test_Wunsch_p2(self):
        z = Complex(3, 4)
        r, _ = z.polar()
        self.assertEqual(r, 5)

    def test_Wunsch_p2_2(self):
        z1 = Complex(3, 4)
        actual = z1 * Complex(1,2) + 2*Complex(0,1)
        r, _ = actual.polar()
        self.assertEqual(r, 13)

    def test_Wunsch_p2_3(self):
        z1 = Complex(1, 3)
        actual = z1.pow(-2) / Complex(2, -3) - Complex(3, 4)
        self.assertTrue(actual.nearly_eq(Complex(-2.9985, -4.0277)))

if __name__ == '__main__':
    unittest.main()
