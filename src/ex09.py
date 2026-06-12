from matrix import Matrix
from ex00 import test


def main():

    # transpose
    test("Transpose 1x1", lambda: (
        Matrix([[42.0]]).transpose().print()
    ))
    # [[42]]

    test("Transpose 2x2", lambda: (
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).transpose().print()
    ))
    # [[1, 3],
    #  [2, 4]]

    test("Transpose 3x3", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]).transpose().print()
    ))
    # [[1, 4, 7],
    #  [2, 5, 8],
    #  [3, 6, 9]]

    test("Transpose rectangular 2x3", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).transpose().print()
    ))
    # [[1, 4],
    #  [2, 5],
    #  [3, 6]]

    test("Transpose rectangular 3x2", lambda: (
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ]).transpose().print()
    ))
    # [[1, 3, 5],
    #  [2, 4, 6]]

    test("Transpose identity matrix", lambda: (
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).transpose().print()
    ))
    # unchanged

    test("Transpose zero matrix", lambda: (
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).transpose().print()
    ))
    # unchanged

    test("Transpose with negative values", lambda: (
        Matrix([
            [-1.0, -2.0],
            [3.0, -4.0]
        ]).transpose().print()
    ))
    # [[-1, 3],
    #  [-2, -4]]


if __name__ == "__main__":
    main()
