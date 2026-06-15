from matrix import Matrix
from typing import TypeVar
from math import tan


K = TypeVar('K', int, float)


def projection(fov:K, ratio:K, near:K, far:K) -> Matrix[K]:
    proj = [[0 for _ in range(4)] for _ in range(4)]
    proj[0][0] = 1 / (ratio * tan(fov / 2))
    proj[1][1] = 1 / tan(fov / 2)
    proj[2][2] = - (far + near) / (far - near)
    proj[2][3] = -1
    proj[3][2] = - (2 * far * near) / (far - near)
    return Matrix(proj)
