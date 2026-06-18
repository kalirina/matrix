from matrix import Matrix
from ex00 import test


def main():

    # transpose
    test("Transpose 1x1", lambda: (
        res := Matrix([[42.0]]).transpose(),
        res.print(),
        print("OK" if res.data == [[42.0]] else "KO")
    ))

    test("Transpose 2x2", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [[1.0, 3.0], [2.0, 4.0]] else "KO")
    ))

    test("Transpose 3x3", lambda: (
        res := Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 4.0, 7.0],
            [2.0, 5.0, 8.0],
            [3.0, 6.0, 9.0]
        ] else "KO")
    ))

    test("Transpose rectangular 2x3", lambda: (
        res := Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 4.0],
            [2.0, 5.0],
            [3.0, 6.0]
        ] else "KO")
    ))

    test("Transpose rectangular 3x2", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 3.0, 5.0],
            [2.0, 4.0, 6.0]
        ] else "KO")
    ))

    test("Transpose identity matrix", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ] else "KO")
    ))

    test("Transpose zero matrix", lambda: (
        res := Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [0.0, 0.0],
            [0.0, 0.0]
        ] else "KO")
    ))

    test("Transpose with negative values", lambda: (
        res := Matrix([
            [-1.0, -2.0],
            [3.0, -4.0]
        ]).transpose(),
        res.print(),
        print("OK" if res.data == [
            [-1.0, 3.0],
            [-2.0, -4.0]
        ] else "KO")
    ))


if __name__ == "__main__":
    main()
