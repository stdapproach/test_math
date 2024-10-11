import cmath
import math


def isNearlyEqual(a: float, b: float, fraction=0.05):
    return abs(a - b) < abs(fraction * a)

def isNearlyEqualByMod(a: float, b: float, modulus: float, fraction=0.05):
    a1 = divmod(a, modulus)[1]
    b1 = divmod(b, modulus)[1]
    return abs(a1 - b1) < abs(fraction * a1)

def foo():
    return 42

class Complex(object):

    def __init__(self, a: float, b=0.0):
        '''Creates Complex Number'''
        self.z = complex(a,b)

    def __str__(self):
        '''Returns complex number as a string'''
        return f"({self.z.real}, {self.z.imag})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            if isinstance(other, (int, float)):
                if self.z.imag == 0:
                    return self.z.real == other
                else:
                    return False
            return False

    def nearly_eq(self, rhs, fraction=0.0001):
        if isinstance(rhs, (int, float)):
            rhs = Complex(rhs, 0)
        z = self - rhs
        r, _ = z.polar()
        r0, _ = self.polar()
        return abs(r) < fraction * r0

    def __add__(self, rhs):
        '''Adds complex numbers'''
        if isinstance(rhs, (int, float)):
            return Complex(self.z.real + rhs, self.z.imag)
        else:
            return Complex(self.z.real + rhs.z.real, self.z.imag + rhs.z.imag)

    def __sub__(self, rhs):
        if isinstance(rhs, (int, float)):
            return Complex(self.z.real - rhs, self.z.imag)
        else:
            return Complex(self.z.real - rhs.z.real, self.z.imag - rhs.z.imag)

    def __mul__(self, rhs):
        if isinstance(rhs, (int, float)):
            return Complex(self.z.real * rhs, self.z.imag * rhs)
        else:
            return Complex(self.z.real * rhs.z.real - self.z.imag * rhs.z.imag, self.z.real * rhs.z.imag + self.z.imag * rhs.z.real)

    def __rmul__(self, rhs):
        if isinstance(rhs, (int, float)):
            return Complex(self.z.real * rhs, self.z.imag * rhs)
        else:
            return Complex(self.z.real * rhs.z.real - self.z.imag * rhs.z.imag, self.z.real * rhs.z.imag + self.z.imag * rhs.z.real)

    def __truediv__(self, rhs):
        if isinstance(rhs, (int, float)):
            return Complex(self.z.real / rhs, self.z.imag / rhs)
        else:
            a = self.z.real
            b = self.z.imag
            c = rhs.z.real
            d = rhs.z.imag
            denom = c*c + d*d
            return Complex((a*c+b*d)/denom, (b*c-a*d)/denom)

    def conj(self):
        return Complex(self.z.real, -self.z.imag)

    def pow(self, n: float):
        if n == 0:
            return Complex(1,0)
        if n == 1:
            return self
        r, arg = self.polar()
        r1 = math.pow(r, n)
        arg1 = n * arg
        return Complex.from_polar((r1, arg1))

    def Ln(self):
        r, arg = self.polar()
        return Complex(math.log(r), arg)

    def root1(self, n: int):
        assert n >= 1
        if n == 1:
            return self
        if self.z.imag == 0:
            if self.z.real >= 0:
                return Complex(math.pow(self.z.real, 1/n))
            else: # <0
                if n == 2:
                    return Complex(0, math.pow(-self.z.real, 1/n))

        r, arg = self.polar()
        r1 = math.pow(r, 1/n)
        arg1 = arg / n
        return Complex.from_polar((r1, arg1))

    def root(self, n: int):
        assert n >= 1
        if n==1 or (self.z.imag == 0 and self.z.real >= 0):
            return [self.root1(n)]

        r, arg = self.polar()
        r1 = math.pow(r, 1 / n)
        arg0 = arg / n
        arg1 = [arg0]
        modulus = 2 * math.pi
        for i in range(1, n):
            arg1.append(arg0 + modulus * i/n)
        #
        #arg2 = [divmod(x, modulus)[1] for x in arg1]
        res = [Complex.from_polar((r1, x)) for x in arg1]
        return res

    def pow_ratio(self, a: float, b: int):
        z0 = self.pow(a)
        return z0.root(b)

    def pow_ratio1(self, a: float, b: int):
        z0 = self.pow(a)
        return z0.root1(b)

    def re(self):
        return self.z.real

    def im(self):
        return self.z.imag

    def is_none(self):
        return self.re() is None or self.im() is None

    def polar(self):
        a = self.z.real
        b = self.z.imag
        r = math.hypot(a, b)
        theta = math.atan2(b, a)
        return r, theta

    @staticmethod
    def from_polar(tup: tuple):
        r = tup[0]
        assert r >= 0
        angl = tup[1]
        z = r * cmath.exp(1j * angl)
        return Complex(z.real, z.imag)

    @staticmethod
    def exp(z):
        r = math.exp(z.re())
        arg = z.im()
        return Complex.from_polar((r, arg))

    def cos(self):
        i = Complex(0, 1)
        z1 = Complex.exp(i*self)
        z2 = Complex.exp(-i * self)
        return (z1+z2)/2

    def sin(self):
        i = Complex(0, 1)
        z1 = Complex.exp(i*self)
        z2 = Complex.exp(-i * self)
        return (z1-z2)/(i * 2)

if __name__ == '__main__':
    z = complex(0,1)
    print(f"Hello from Python/Bazel!,j={z}")
