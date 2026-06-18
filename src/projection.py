from matrix import Matrix
from typing import TypeVar
from math import tan


K = TypeVar('K', int, float)


def projection(fov:K, ratio:K, near:K, far:K) -> Matrix[K]:
    if near <= 0:
        raise ValueError("near must be positive")
    if far <= near:
        raise ValueError("far must be greater than near")
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    proj = [[0.0 for _ in range(4)] for _ in range(4)]
    f = 1 / tan(fov / 2)
    proj[0][0] = f / ratio
    proj[1][1] = f
    proj[2][2] = far / (far - near)
    proj[2][3] = 1.0
    proj[3][2] = - (near * far) / (far - near)
    return Matrix(proj)
