from typing import TypeVar, Generic, List
from vector import Vector
from complex import Complex


K = TypeVar('K', int, float, Complex)

class Matrix(Generic[K]):
    def __init__(self,data:List[List[K]]):
        if len(data) == 0 or any(not isinstance(row,list) for row in data) \
            or any(len(row) == 0 for row in data) \
            or any(len(row) != len(data[0]) for row in data):
            raise TypeError("Invaid matrix form")
        t = type(data[0][0])
        for row in data:
            for el in row:
                if type(el) != t:
                    raise TypeError("Mixed types in matrix")
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
            print(row)

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
        res:List[K] = [self.data[0][0] * 0 for _ in range(self.rows)]
        for r in range(self.rows):
            tmp:K = self.data[0][0] * 0
            for c in range(self.cols):
                tmp += self.data[r][c] * vec.data[c]
            res[r] = tmp
        return Vector(res)

    def mul_mat(self, mat:'Matrix[K]') -> 'Matrix[K]':
        if self.cols != mat.rows:
            raise ValueError("Matrices of incompatible size")
        res:List[List[K]] = [[self.data[0][0] * 0 for _ in range(mat.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(mat.cols):
                tmp: K = self.data[0][0] * 0
                for k in range(self.cols):
                     tmp += self.data[r][k] * mat.data[k][c]
                res[r][c] = tmp
        return Matrix(res)

    # ex08
    def trace(self) -> K:
        if not self.square():
            raise ValueError("Matrix must be square")
        trace:K = self.data[0][0] * 0
        for r in range(self.rows):
            trace += self.data[r][r]
        return trace

    # ex09
    def transpose(self) -> 'Matrix[K]':
        res:List[List[K]] = [[ self.data[0][0] * 0 for _ in range(self.rows)] for _ in range(self.cols)]
        for r in range(self.rows):
            for c in range(self.cols):
                res[c][r] = self.data[r][c]
        return Matrix(res)

    def is_zero(x):
        return abs(x) == 0

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
                if not self.is_zero(data[r][p_c]):
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
                if not self.is_zero(a):
                    sub_scaled_row(r, p_r, a)
            pivots.append((p_r, p_c))
            p_r += 1
            if p_r == self.rows:
                break
        # eliminate above
        for r, c in reversed(pivots):
            for i in range(r - 1, -1, -1):
                if not self.is_zero(data[i][c]):
                    factor = data[i][c]
                    sub_scaled_row(i, r, factor)
        return Matrix(data)

    # ex11
    def determinant(self):
        if not self.square():
            raise ValueError("Matrix must be square")
        if self.rows > 4:
            raise ValueError("Maximum matrix size is 4")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det:K = self.data[0][0] * 0
        for c in range(self.cols):
            minor = []
            for r in range(1, self.rows):
                row = []
                for j in range(self.cols):
                    if j != c:
                        row.append(self.data[r][j])
                minor.append(row)
            sign = 1 if c % 2 == 0 else -1
            det += sign * self.data[0][c] * Matrix(minor).determinant()
        return det

    # ex12
    def inverse(self) -> 'Matrix[K]':
        if not self.square():
            raise ValueError("Matrix must be square")
        if abs(self.determinant()) < 1e-12:
            raise ValueError("Matrix doesn't have an inverse")
        inv = [[1 if j == i else 0 for j in range(self.cols)] for i in range(self.rows)]
        data = [row[:] for row in self.data]
        def swap_rows(mat, i, j):
            mat[i], mat[j] = mat[j], mat[i]
        def scale_row(mat, i, a):
            for c in range(self.cols):
                mat[i][c] *= a
        def sub_scaled_row(mat, dest, sour, a):
            for c in range(self.cols):
                mat[dest][c] -= mat[sour][c] * a
        p_r = 0
        pivots = []
        for p_c in range(self.cols):
            # find pivot column in row r
            pivot = None
            for r in range(p_r, self.rows):
                if not self.is_zero(data[r][p_c]):
                    pivot = r
                    break
            if pivot is None:
                continue
            # put in place and turn to 1 pivot
            swap_rows(data, p_r, pivot)
            swap_rows(inv, p_r, pivot)
            factor = 1 / data[p_r][p_c]
            scale_row(data, p_r, factor)
            scale_row(inv, p_r, factor)
            # eliminate below
            for r in range(p_r + 1, self.rows):
                a = data[r][p_c]
                if not self.is_zero(a):
                    sub_scaled_row(data, r, p_r, a)
                    sub_scaled_row(inv, r, p_r, a)
            pivots.append((p_r, p_c))
            p_r += 1
            if p_r == self.rows:
                break
        # eliminate above
        for r, c in reversed(pivots):
            for i in range(r - 1, -1, -1):
                if not self.is_zero(data[i][c]):
                    factor = data[i][c]
                    sub_scaled_row(data, i, r, factor)
                    sub_scaled_row(inv, i, r, factor)
        return Matrix(inv)

    # ex13
    def rank(self):
        echelon = self.row_echelon()
        rank = 0
        for row in echelon.data:
            if any(not self.is_zero(el) for el in row):
                rank += 1
        return rank
