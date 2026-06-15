from matrix import Matrix
from ex00 import test


def main():

    # trace (subject examples)
    test("Trace identity 2x2", lambda: print(
        Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ]).trace()
    ))  # 2

    test("Trace subject 3x3 #1", lambda: print(
        Matrix([
            [2.0, -5.0, 0.0],
            [4.0, 3.0, 7.0],
            [-2.0, 3.0, 4.0]
        ]).trace()
    ))  # 9

    test("Trace subject 3x3 #2", lambda: print(
        Matrix([
            [-2.0, -8.0, 4.0],
            [1.0, -23.0, 4.0],
            [0.0, 6.0, 4.0]
        ]).trace()
    ))  # -21

    # extra
    test("Trace 1x1", lambda: print(
        Matrix([[42.0]]).trace()
    ))  # 42

    test("Trace zero matrix", lambda: print(
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).trace()
    ))  # 0

    test("Trace with negatives", lambda: print(
        Matrix([
            [-1.0, 2.0],
            [3.0, -4.0]
        ]).trace()
    ))  # -5

    # errors
    test("Trace non-square matrix", lambda: print(
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).trace()
    ))


if __name__ == "__main__":
    main()
