from vector import Vector
from ex00 import test


def main():
    test("Dot basic 2D", lambda: print(
        Vector([1.0, 2.0]).dot(Vector([3.0, 4.0]))
    ))  # 1*3 + 2*4 = 11
    test("Dot basic 3D", lambda: print(
        Vector([1.0, 2.0, 3.0]).dot(Vector([4.0, 5.0, 6.0]))
    ))  # 32

    # edges
    test("Dot with zero vector", lambda: print(
        Vector([1.0, 2.0, 3.0]).dot(Vector([0.0, 0.0, 0.0]))
    ))  # 0
    test("Dot identical vectors", lambda: print(
        Vector([2.0, 3.0, 4.0]).dot(Vector([2.0, 3.0, 4.0]))
    ))  # 29
    test("Dot orthogonal vectors", lambda: print(
        Vector([1.0, 0.0]).dot(Vector([0.0, 1.0]))
    ))  # 0

    # errors
    test("Dot size mismatch", lambda: (
        Vector([1.0, 2.0]).dot(Vector([1.0, 2.0, 3.0]))
    ))
    test("Dot type mismatch", lambda: (
        Vector([1, 2, 3]).dot(Vector([1.0, 2.0, 3.0]))
    ))


if __name__ == "__main__":
    main()
