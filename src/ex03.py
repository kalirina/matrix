from vector import Vector
from ex00 import test


def main():
    # dot (subject examples)
    test("Dot subject 1", lambda: (
        res := Vector([0.0, 0.0]).dot(Vector([1.0, 1.0])),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Dot subject 2", lambda: (
        res := Vector([1.0, 1.0]).dot(Vector([1.0, 1.0])),
        print(res),
        print("OK" if res == 2.0 else "KO")
    ))

    test("Dot subject 3", lambda: (
        res := Vector([-1.0, 6.0]).dot(Vector([3.0, 2.0])),
        print(res),
        print("OK" if res == 9.0 else "KO")
    ))

    # dot basic
    test("Dot basic 2D", lambda: (
        res := Vector([1.0, 2.0]).dot(Vector([3.0, 4.0])),
        print(res),
        print("OK" if res == 11.0 else "KO")
    ))

    test("Dot basic 3D", lambda: (
        res := Vector([1.0, 2.0, 3.0]).dot(Vector([4.0, 5.0, 6.0])),
        print(res),
        print("OK" if res == 32.0 else "KO")
    ))

    # edges
    test("Dot with zero vector", lambda: (
        res := Vector([1.0, 2.0, 3.0]).dot(Vector([0.0, 0.0, 0.0])),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Dot identical vectors", lambda: (
        res := Vector([2.0, 3.0, 4.0]).dot(Vector([2.0, 3.0, 4.0])),
        print(res),
        print("OK" if res == 29.0 else "KO")
    ))

    test("Dot orthogonal vectors", lambda: (
        res := Vector([1.0, 0.0]).dot(Vector([0.0, 1.0])),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Dot different type", lambda: (
        res := Vector([1, 2, 3]).dot(Vector([1.0, 2.0, 3.0])),
        print(res),
        print("OK" if res == 14.0 else "KO")
    ))

    # errors
    test("Dot size mismatch", lambda: (
        Vector([1.0, 2.0]).dot(Vector([1.0, 2.0, 3.0]))
    ))


if __name__ == "__main__":
    main()
