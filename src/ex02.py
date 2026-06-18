from vector import Vector
from matrix import Matrix
from linear_algebra import lerp
from ex00 import test


def main():
    # scalar
    test("Subject Lerp scalar basic", lambda: (res := lerp(0.0, 1.0, 0.0), print(res), print("OK" if res == 0.0 else "KO")))

    test("Subject Lerp scalar mid", lambda: (res := lerp(0.0, 1.0, 0.5), print(res), print("OK" if res == 0.5 else "KO")))

    test("Subject Lerp scalar end", lambda: (res := lerp(0.0, 1.0, 1.0), print(res), print("OK" if res == 1.0 else "KO")))

    test("Subject Lerp scalar custom", lambda: (res := lerp(21.0, 42.0, 0.3), print(res), print("OK" if res == 27.3 else "KO")))

    test("Lerp scalar identical", lambda: (res := lerp(5.0, 5.0, 0.5), print(res), print("OK" if res == 5.0 else "KO")))

    test("Lerp scalar extrapolate low", lambda: (res := lerp(0.0, 1.0, -1.0), print(res), print("OK" if res == -1.0 else "KO")))

    test("Lerp scalar extrapolate high", lambda: (res := lerp(0.0, 1.0, 2.0), print(res), print("OK" if res == 2.0 else "KO")))

    # vectors
    test("Subject Lerp vector 2D", lambda: (
        (v1 := Vector([2.0, 1.0])),
        (v2 := Vector([4.0, 2.0])),
        (res := lerp(v1, v2, 0.3)),
        res.print(),
        print("OK" if res.data == [2.6, 1.3] else "KO")
    ))

    test("Lerp vector 3D", lambda: (
        (v1 := Vector([1.0, 2.0, 3.0])),
        (v2 := Vector([4.0, 5.0, 6.0])),
        (res := lerp(v1, v2, 0.5)),
        res.print(),
        print("OK" if res.data == [2.5, 3.5, 4.5] else "KO")
    ))

    test("Lerp vector identical", lambda: (
        (v1 := Vector([1.0, 2.0, 3.0])),
        (res := lerp(v1, v1, 0.5)),
        res.print(),
        print("OK" if res.data == [1.0, 2.0, 3.0] else "KO")
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
        (res := lerp(m1, m2, 0.5)),
        res.print(),
        print("OK" if res.data == [[11.0, 5.5], [16.5, 22.0]] else "KO")
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
        (res := lerp(m1, m2, 0.5)),
        res.print(),
        print("OK" if res.data == [[5.0, 5.0, 5.0],[5.0, 5.0, 5.0],[5.0, 5.0, 5.0]] else "KO")
    ))

    test("Lerp matrix identical", lambda: (
        (m1 := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (res := lerp(m1, m1, 0.5)),
        res.print(),
        print("OK" if res.data == [[1.0, 2.0], [3.0, 4.0]] else "KO")
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
