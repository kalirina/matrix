from typing import TypeVar, Generic, List
from vector import Vector

K = TypeVar('K',int,float)

class Matrix(Generic[K]):
    def __init__(self,data:List[List[K]]):
        if len(data) == 0 or any(not isinstance(row,list) for row in data) \
            or any(len(row) == 0 for row in data) \
            or any(len(row) != len(data[0]) for row in data):
            raise TypeError("Invaid matrix form")
        self.data:List[List[K]] = data
        self.shape()

    def size(self):
        size = 0
        for row in self.data:
            for col in row:
                size += 1
        return size

    def print(self):
        for row in self.data:
            print([0.0 if abs(x) < 1e-12 else x for x in row])

    def shape(self):
        self.rows = 0
        for row in self.data:
            self.rows += 1
        self.cols = 0
        for col in self.data[0]:
            self.cols += 1

    def square(self):
        if self.rows == self.cols:
            return True
        return False

    # ex00
    def add(self, v:'Matrix[K]'):
        if self.rows != v.rows or self.cols != v.cols:
            raise TypeError("Matrices not of same size")
        if type(self.data[0][0]) != type(v.data[0][0]):
            raise TypeError("Matrices not of same type")
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] += v.data[r][c]

    def sub(self, v:'Matrix[K]'):
        if self.rows != v.rows or self.cols != v.cols:
            raise TypeError("Matrices not of same size")
        if not isinstance(self.data[0], type(v.data[0])):
            raise TypeError("Matrices not of same type")
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] -= v.data[r][c]

    def scl(self, a:K):
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] *= a

    # ex07
    def mul_vec(self, vec:'Vector[K]') -> 'Vector[K]':
        if self.cols != vec.size():
            raise ValueError("Matrix and vector of incompatible size")
        res:List[K] = [0 for _ in range(self.rows)]
        for r in range(self.rows):
            tmp:K = 0
            for c in range(self.cols):
                tmp += self.data[r][c] * vec.data[c]
            res[r] = tmp
        return Vector(res)

    def mul_mat(self, mat:'Matrix[K]') -> 'Matrix[K]':
        if self.cols != mat.rows:
            raise ValueError("Matrices of incompatible size")
        res:List[List[K]] = [[ 0 for _ in range(mat.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(mat.cols):
                tmp: K = 0
                for k in range(self.cols):
                     tmp += self.data[r][k] * mat.data[k][c]
                res[r][c] = tmp
        return Matrix(res)

    # ex08
    def trace(self) -> K:
        if not self.square():
            raise ValueError("Matrix must be square")
        trace:K = 0
        for r in range(self.rows):
            trace += self.data[r][r]
        return trace

    # ex09
    def transpose(self) -> 'Matrix[K]':
        res:List[List[K]] = [[ 0 for _ in range(self.rows)] for _ in range(self.cols)]
        for r in range(self.rows):
            for c in range(self.cols):
                res[c][r] = self.data[r][c]
        return Matrix(res)

    # ex10
    def row_echelon(self) -> 'Matrix[K]':
        data = [row[:] for row in self.data]
        def swap_rows(i, j):
            data[i], data[j] = data[j], data[i]
        def scale_row(i, a):
            for c in range(self.cols):
                data[i][c] *= a
        def sub_scaled_row(dest, sour, a):
            for c in range(self.cols):
                data[dest][c] -= data[sour][c] * a
        p_r = 0
        pivots = []
        for p_c in range(self.cols):
            # find pivot column in row r
            pivot = None
            for r in range(p_r, self.rows):
                if data[r][p_c] != 0:
                    pivot = r
                    break
            if pivot is None:
                continue
            # put in place and turn to 1 pivot
            swap_rows(p_r, pivot)
            scale_row(p_r, 1 / data[p_r][p_c])
            # eliminate below
            for r in range(p_r + 1, self.rows):
                a = data[r][p_c]
                if a != 0:
                    sub_scaled_row(r, p_r, a)
            pivots.append((p_r, p_c))
            p_r += 1
            if p_r == self.rows:
                break
        # eliminate above
        for r, c in reversed(pivots):
            for i in range(r - 1, -1, -1):
                if data[i][c] != 0:
                    factor = data[i][c]
                    sub_scaled_row(i, r, factor)
        return Matrix(data)
