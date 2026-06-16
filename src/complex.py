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
