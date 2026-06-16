from typing import TypeVar, List
from vector import Vector
from matrix import Matrix

K = TypeVar('K', int, float)
V = TypeVar('V', int, float, 'Vector', 'Matrix')

# ex01
def linear_combination(u:List[Vector[K]],coefs:List[K]) -> 'Vector[K]':
    if len(u) == 0 or len(coefs) == 0:
        raise ValueError("Empty argument list")
    if len(u) != len(coefs):
        raise ValueError("Arguments not of same size")
    if not all(vector.size() == u[0].size() for vector in u):
        raise ValueError("Vectors not of same size")
    result:List[K] = [u[0].data[0] * 0 for _ in range(u[0].size())]
    for i in range(len(coefs)):
        for j in range(u[0].size()):
            result[j] += u[i].data[j] * coefs[i]
    return Vector(result)

# ex02
def lerp(u:V, v:V, t:K) -> V:
    if type(u) != type(v):
        raise TypeError("Arguments not of same size")
    if not(isinstance(t, (int, float))) or t > 1 or t < 0:
        raise ValueError("Wrong scalar")
    if isinstance(u, Vector):
        if u.size() != v.size():
            raise ValueError("Vectors not of same size")
        res = [a * (1 - t) + b * t for a, b in zip(u.data, v.data)]
        return Vector(res)
    elif isinstance(u, Matrix):
        if u.rows != v.rows or u.cols != v.cols:
            raise ValueError("Matrices not of same size")
        res = [ [ u.data[r][c] * (1 - t) + v.data[r][c] * t
                for c in range(u.cols) ]
                    for r in range(u.rows)]
        return Matrix(res)
    elif isinstance(u, (int, float)):
        return u * (1 - t) + t * v
    raise TypeError("Unsupported type for lerp")

# ex05
def angle_cos(u:Vector[K], v:Vector[K]) -> K:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Argument is not of Vector type")
    if u.size() != v.size():
        raise ValueError("Vectors not of same size")
    if all(value== 0 for value in u.data) or all(value == 0 for value in v.data):
        raise ValueError("Argument is zero")
    if not isinstance(u.data[0], type(v.data[0])):
        raise TypeError("Vectors not of same type")
    return (u.dot(v)) / (u.norm() * v.norm())

# ex06
def cross_product(u:Vector[K], v:Vector[K]) -> Vector[K]:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Argument is not of Vector type")
    if u.size() != v.size():
        raise ValueError("Vectors not of same size")
    if u.size() != 3:
        raise ValueError("Vectors size shoud be 3")
    if not isinstance(u.data[0], type(v.data[0])):
        raise TypeError("Vectors not of same type")
    return Vector([
        u.data[1] * v.data[2] - u.data[2] * v.data[1],
        u.data[2] * v.data[0] - u.data[0] * v.data[2],
        u.data[0] * v.data[1] - u.data[1] * v.data[0]
    ])
