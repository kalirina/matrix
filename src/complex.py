class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.re * other, self.im * other)
        if isinstance(other, Complex):
            return Complex(
                self.re * other.re - self.im * other.im,
                self.re * other.im + self.im * other.re
            )
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        if isinstance(other, Complex):
            denom = other.re * other.re + other.im * other.im
            return Complex(
                (self.re * other.re + self.im * other.im) / denom,
                (self.im * other.re - self.re * other.im) / denom
            )
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return False
        return self.re == other.re and self.im == other.im

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __repr__(self):
        return self.__str__()

    def __abs__(self):
        return (self.re * self.re + self.im * self.im) ** 0.5

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.re += other
            return self
        if isinstance(other, Complex):
            self.re += other.re
            self.im += other.im
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.re -= other
            return self
        if isinstance(other, Complex):
            self.re -= other.re
            self.im -= other.im
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.re *= other
            self.im *= other
            return self
        if isinstance(other, Complex):
            a, b = self.re, self.im
            c, d = other.re, other.im
            self.re = a * c - b * d
            self.im = a * d + b * c
            return self
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        if isinstance(other, Complex):
            a, b = self.re, self.im
            c, d = other.re, other.im
            denom = c * c + d * d
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            self.re = (a * c + b * d) / denom
            self.im = (b * c - a * d) / denom
            return self
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other, 0) - self
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other, 0) / self
        return NotImplemented

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("Only integer powers supported")
        if n == 0:
            return Complex(1, 0)
        result = Complex(self.re, self.im)
        for _ in range(n - 1):
            result *= self
        return result
