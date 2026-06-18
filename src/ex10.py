from matrix import Matrix
from ex00 import test


def main():

    # identity matrix
    test("Subject Row echelon identity 3x3", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ] else "KO")
    ))

    # 2x2 full rank
    test("Subject Row echelon 2x2 full rank", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0],
            [-0.0, 1.0]
        ] else "KO")
    ))

    # dependent rows
    test("Subject Row echelon dependent rows", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 2.0],
            [0.0, 0.0]
        ] else "KO")
    ))

    # full subject example (3x5 matrix)
    test("Subject Row echelon 3x5 subject case", lambda: (
        res := Matrix([
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.625, 0.0, 0.0, -12.166666666666666],
            [0.0, 0.0, 1.0, 0.0, -3.6666666666666665],
            [-0.0, -0.0, -0.0, 1.0, 29.5]
        ] else "KO")
    ))

    # zero matrix
    test("Row echelon zero matrix", lambda: (
        res := Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [0.0, 0.0],
            [0.0, 0.0]
        ] else "KO")
    ))

    # matrix with zero column
    test("Row echelon with zero column", lambda: (
        res := Matrix([
            [0.0, 2.0, 3.0],
            [0.0, 0.0, 1.0],
            [0.0, 5.0, 6.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, 0.0]
        ] else "KO")
    ))

    # requires row swap
    test("Row echelon with row swap", lambda: (
        res := Matrix([
            [0.0, 2.0, 1.0],
            [1.0, 3.0, 4.0],
            [2.0, 5.0, 6.0]
        ]).row_echelon(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [-0.0, -0.0, 1.0]
        ] else "KO")
    ))


if __name__ == "__main__":
    main()
