from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Determinant 2x2 subject", lambda: print(
        Matrix([
            [1.0, -1.0],
            [-1.0, 1.0]
        ]).determinant()
    ))  # 0.0

    test("Determinant 3x3 diagonal subject", lambda: print(
        Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ]).determinant()
    ))  # 8.0

    test("Determinant 3x3 subject", lambda: print(
        Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ]).determinant()
    ))  # -174.0

    test("Determinant 4x4 subject", lambda: print(
        Matrix([
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0]
        ]).determinant()
    ))  # 1032.0

    # edge cases

    test("Determinant 1x1", lambda: print(
        Matrix([
            [42.0]
        ]).determinant()
    ))  # 42.0


    test("Determinant identity 3x3", lambda: print(
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).determinant()
    ))  # 1.0

    test("Determinant zero matrix", lambda: print(
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).determinant()
    ))  # 0.0

    test("Determinant dependent rows", lambda: print(
        Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).determinant()
    ))  # 0.0

    test("Determinant non-square", lambda: print(
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).determinant()
    ))

    test("Determinant size > 4", lambda: print(
        Matrix([
            [1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0]
        ]).determinant()
    ))


if __name__ == "__main__":
    main()
