class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        if not isinstance(other, Complex):
            return Complex(self.re + other, self.im)
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            return Complex(self.re - other, self.im)
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            return Complex(self.re * other, self.im * other)
        return Complex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re
        )

    def __truediv__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other, 0)

        denom = other.re**2 + other.im**2
        return Complex(
            (self.re * other.re + self.im * other.im) / denom,
            (self.im * other.re - self.re * other.im) / denom
        )

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return False
        return self.re == other.re and self.im == other.im

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __repr__(self):
        return self.__str__()

    def __abs__(self):
        return (self.re**2 + self.im**2) ** 0.5

    def __iadd__(self, other):
        if not isinstance(other, Complex):
            self.re += other
            return self
        self.re += other.re
        self.im += other.im
        return self

    def __isub__(self, other):
        if not isinstance(other, Complex):
            self.re -= other
            return self
        self.re -= other.re
        self.im -= other.im
        return self

    def __imul__(self, other):
        if not isinstance(other, Complex):
            self.re *= other
            self.im *= other
            return self
        a, b = self.re, self.im
        c, d = other.re, other.im

        self.re = a * c - b * d
        self.im = a * d + b * c
        return self

    def __itruediv__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other, 0)
        a, b = self.re, self.im
        c, d = other.re, other.im

        denom = c * c + d * d
        if denom == 0:
            raise ZeroDivisionError("division by zero")

        self.re = (a * c + b * d) / denom
        self.im = (b * c - a * d) / denom
        return self

    def __rmul__(self, other):
        return self * other

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Complex(other, 0) - self

    def __rtruediv__(self, other):
        return Complex(other, 0) / self
