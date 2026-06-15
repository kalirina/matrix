from vector import Vector
from matrix import Matrix
from linear_algebra import lerp
from ex00 import test


def main():
    # scalar
    test("Subject Lerp scalar basic", lambda: print(lerp(0.0, 1.0, 0.0)))

    test("Subject Lerp scalar mid", lambda: print(lerp(0.0, 1.0, 0.5)))

    test("Subject Lerp scalar end", lambda: print(lerp(0.0, 1.0, 1.0)))

    test("Subject Lerp scalar custom", lambda: print(lerp(21.0, 42.0, 0.3)))

    test("Lerp scalar identical", lambda: print(lerp(5.0, 5.0, 0.5)))

    test("Lerp scalar extrapolate low", lambda: print(lerp(0.0, 1.0, -1.0)))

    test("Lerp scalar extrapolate high", lambda: print(lerp(0.0, 1.0, 2.0)))

    # vectors
    test("Subject Lerp vector 2D", lambda: (
        (v1 := Vector([2.0, 1.0])),
        (v2 := Vector([4.0, 2.0])),
        lerp(v1, v2, 0.3).print()
    ))

    test("Lerp vector 3D", lambda: (
        (v1 := Vector([1.0, 2.0, 3.0])),
        (v2 := Vector([4.0, 5.0, 6.0])),
        lerp(v1, v2, 0.5).print()
    ))

    test("Lerp vector identical", lambda: (
        (v1 := Vector([1.0, 2.0, 3.0])),
        lerp(v1, v1, 0.5).print()
    ))

    test("Lerp vector size mismatch", lambda: (
        (v1 := Vector([1.0, 2.0])),
        (v2 := Vector([1.0, 2.0, 3.0])),
        lerp(v1, v2, 0.5).print()
    ))

    # matrices
    test("Subject Lerp matrix 2x2", lambda: (
        (m1 := Matrix([[2.0, 1.0], [3.0, 4.0]])),
        (m2 := Matrix([[20.0, 10.0], [30.0, 40.0]])),
        lerp(m1, m2, 0.5).print()
    ))

    test("Lerp matrix 3x3", lambda: (
        (m1 := Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ])),
        (m2 := Matrix([
            [9.0, 8.0, 7.0],
            [6.0, 5.0, 4.0],
            [3.0, 2.0, 1.0]
        ])),
        lerp(m1, m2, 0.5).print()
    ))

    test("Lerp matrix identical", lambda: (
        (m1 := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        lerp(m1, m1, 0.5).print()
    ))

    test("Lerp matrix size mismatch", lambda: (
        (m1 := Matrix([[1.0, 2.0]])),
        (m2 := Matrix([[1.0], [2.0]])),
        lerp(m1, m2, 0.5).print()
    ))

    test("Lerp type mismatch", lambda: (
        (v1 := Vector([1.0, 2.0])),
        (m2 := Matrix([[1.0], [2.0]])),
        lerp(v1, m2, 0.5).print()
    ))

if __name__ == "__main__":
    main()
