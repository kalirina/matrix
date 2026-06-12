from matrix import Matrix
from ex00 import test


def main():

    # trace
    test("Trace 1x1", lambda: print(
        Matrix([[42.0]]).trace()
    ))  # 42

    test("Trace 2x2", lambda: print(
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).trace()
    ))  # 5

    test("Trace 3x3", lambda: print(
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]).trace()
    ))  # 15

    test("Trace identity matrix", lambda: print(
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).trace()
    ))  # 3

    test("Trace zero matrix", lambda: print(
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).trace()
    ))  # 0

    test("Trace with negative values", lambda: print(
        Matrix([
            [-1.0, 2.0],
            [3.0, -4.0]
        ]).trace()
    ))  # -5

    # edges, errors
    test("Trace non-square matrix", lambda: print(
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).trace()
    ))


if __name__ == "__main__":
    main()
