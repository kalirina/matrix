from matrix import Matrix
from ex00 import test


def main():

    # identity matrix
    test("Row echelon identity 3x3", lambda: (
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).row_echelon().print()
    ))

    # 2x2 full rank
    test("Row echelon 2x2 full rank", lambda: (
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).row_echelon().print()
    ))

    # dependent rows
    test("Row echelon dependent rows", lambda: (
        Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).row_echelon().print()
    ))

    # full subject example (3x5 matrix)
    test("Row echelon 3x5 subject case", lambda: (
        Matrix([
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0]
        ]).row_echelon().print()
    ))

    # zero matrix
    test("Row echelon zero matrix", lambda: (
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).row_echelon().print()
    ))

    # matrix with zero column
    test("Row echelon with zero column", lambda: (
        Matrix([
            [0.0, 2.0, 3.0],
            [0.0, 0.0, 1.0],
            [0.0, 5.0, 6.0]
        ]).row_echelon().print()
    ))

    # requires row swap
    test("Row echelon with row swap", lambda: (
        Matrix([
            [0.0, 2.0, 1.0],
            [1.0, 3.0, 4.0],
            [2.0, 5.0, 6.0]
        ]).row_echelon().print()
    ))


if __name__ == "__main__":
    main()
