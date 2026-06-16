from typing import TypeVar, Generic, List
from complex import Complex

K = TypeVar('K', int, float, Complex)

class Vector(Generic[K]):
    def __init__(self,data:List[K]):
        if len(data) == 0:
            raise ValueError("Empty list in Vector initialisation")
        if any(not isinstance(element, type(data[0])) for element in data):
            raise ValueError("Elements in argument are not of same type")
        self.data:List[K] = data

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    # ex00
    def add(self, v:'Vector[K]'):
        if self.size() != v.size():
            raise TypeError("Vectors not of same size")
        self.data = [a + b for a, b in zip(self.data, v.data)]

    def sub(self, v:'Vector[K]'):
        if self.size() != v.size():
            raise TypeError("Vectors not of same size")
        self.data = [a - b for a, b in zip(self.data, v.data)]

    def scl(self, a:K):
        self.data = [v * a for v in self.data]

    # ex03
    def dot(self, v:'Vector[K]') -> K:
        if self.size() != v.size():
            raise ValueError("Vectors not of same size")
        res:K = self.data[0] * 0
        for i in range(self.size()):
            res += self.data[i] * v.data[i]
        return res

    # ex04
    def norm_1(self) -> K:
        res:K = self.data[0] * 0
        for el in self.data:
            res += abs(el)
        return res

    def norm(self):
        res = 0.0
        for el in self.data:
            res += abs(el) ** 2
        return pow(res, 0.5)

    def norm_inf(self) -> K:
        res = abs(self.data[0])
        for el in self.data:
            val = abs(el)
            if val > res:
                res = val
        return res
