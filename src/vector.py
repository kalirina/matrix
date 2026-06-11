from typing import TypeVar, Generic, List

K = TypeVar('K',int,float)

class Vector(Generic[K]):
    def __init__(self,data:List[K]):
        if len(data) == 0:
            raise ValueError("Empty list in Vector initialisation")
        for el in data:
            if not isinstance(el,type(data[0])):
                raise TypeError("Elements in argument are not of same type")
        self.data:List[K] = data

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)

    # ex00
    def add(self,v:'Vector[K]'):
        if self.size() != v.size():
            raise TypeError("Vectors not of same size")
        if not isinstance(self.data[0], type(v.data[0])):
            raise TypeError("Vectors not of same type")
        self.data = [a + b for a, b in zip(self.data, v.data)]

    def sub(self,v:'Vector[K]'):
        if self.size() != v.size():
            raise TypeError("Vectors not of same size")
        if not isinstance(self.data[0], type(v.data[0])):
            raise TypeError("Vectors not of same type")
        self.data = [a - b for a, b in zip(self.data, v.data)]

    def scl(self,a:K):
        self.data = [v * a for v in self.data]
