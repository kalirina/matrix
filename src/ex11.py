from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Determinant 2x2 subject", lambda: (
        res := Matrix([
            [1.0, -1.0],
            [-1.0, 1.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Determinant 3x3 diagonal subject", lambda: (
        res := Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 8.0 else "KO")
    ))

    test("Determinant 3x3 subject", lambda: (
        res := Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ]).determinant(),
        print(res),
        print("OK" if res == -174.0 else "KO")
    ))

    test("Determinant 4x4 subject", lambda: (
        res := Matrix([
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 1032.0 else "KO")
    ))

    # edge cases

    test("Determinant 1x1", lambda: (
        res := Matrix([[42.0]]).determinant(),
        print(res),
        print("OK" if res == 42.0 else "KO")
    ))

    test("Determinant identity 3x3", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))

    test("Determinant zero matrix", lambda: (
        res := Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Determinant dependent rows", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Determinant non-square", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).determinant()
    ))

    test("Determinant size > 4", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0]
        ]).determinant(),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))


if __name__ == "__main__":
    main()
