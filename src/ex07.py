from vector import Vector
from matrix import Matrix
from ex00 import test


def main():
    # mul_vec (subject examples)
    test("Matrix-vector subject 1", lambda: (
        res := Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ]).mul_vec(Vector([4.0, 2.0])),
        res.print(),
        print("OK" if res.data == [4.0, 2.0] else "KO")
    ))

    test("Matrix-vector subject 2", lambda: (
        res := Matrix([
            [2.0, 0.0],
            [0.0, 2.0]
        ]).mul_vec(Vector([4.0, 2.0])),
        res.print(),
        print("OK" if res.data == [8.0, 4.0] else "KO")
    ))

    test("Matrix-vector subject 3", lambda: (
        res := Matrix([
            [2.0, -2.0],
            [-2.0, 2.0]
        ]).mul_vec(Vector([4.0, 2.0])),
        res.print(),
        print("OK" if res.data == [4.0, -4.0] else "KO")
    ))

    # mul_mat (subject examples)
    test("Matrix-matrix subject 1", lambda: (
        res := Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ]).mul_mat(Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ])),
        res.print(),
        print("OK" if res.data == [[1.0, 0.0], [0.0, 1.0]] else "KO")
    ))

    test("Matrix-matrix subject 2", lambda: (
        res := Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ]).mul_mat(Matrix([
            [2.0, 1.0],
            [4.0, 2.0]
        ])),
        res.print(),
        print("OK" if res.data == [[2.0, 1.0], [4.0, 2.0]] else "KO")
    ))

    test("Matrix-matrix subject 3", lambda: (
        res := Matrix([
            [3.0, -5.0],
            [6.0, 8.0]
        ]).mul_mat(Matrix([
            [2.0, 1.0],
            [4.0, 2.0]
        ])),
        res.print(),
        print("OK" if res.data == [[-14.0, -7.0], [44.0, 22.0]] else "KO")
    ))

    # mul_vec

    test("Matrix-vector 2x2", lambda: (
        res := Matrix([[1.0, 2.0], [3.0, 4.0]]).mul_vec(Vector([5.0, 6.0])),
        res.print(),
        print("OK" if res.data == [17.0, 39.0] else "KO")
    ))

    test("Matrix-vector identity", lambda: (
        res := Matrix([[1.0, 0.0], [0.0, 1.0]]).mul_vec(Vector([42.0, 21.0])),
        res.print(),
        print("OK" if res.data == [42.0, 21.0] else "KO")
    ))

    test("Matrix-vector zero matrix", lambda: (
        res := Matrix([[0.0, 0.0], [0.0, 0.0]]).mul_vec(Vector([5.0, 6.0])),
        res.print(),
        print("OK" if res.data == [0.0, 0.0] else "KO")
    ))

    test("Matrix-vector incompatible size", lambda: (
        Matrix([[1.0, 2.0], [3.0, 4.0]]).mul_vec(Vector([1.0, 2.0, 3.0])).print()
    ))

    # mul_mat

    test("Matrix-matrix 2x2", lambda: (
        res := Matrix([[1.0, 2.0], [3.0, 4.0]]).mul_mat(Matrix([[5.0, 6.0], [7.0, 8.0]])),
        res.print(),
        print("OK" if res.data == [[19.0, 22.0], [43.0, 50.0]] else "KO")
    ))

    test("Matrix-matrix identity", lambda: (
        res := Matrix([[1.0, 2.0], [3.0, 4.0]]).mul_mat(Matrix([[1.0, 0.0], [0.0, 1.0]])),
        res.print(),
        print("OK" if res.data == [[1.0, 2.0], [3.0, 4.0]] else "KO")
    ))

    test("Matrix-matrix rectangular", lambda: (
        res := Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).mul_mat(Matrix([
            [7.0, 8.0],
            [9.0, 10.0],
            [11.0, 12.0]
        ])),
        res.print(),
        print("OK" if res.data == [[58.0, 64.0], [139.0, 154.0]] else "KO")
    ))

    test("Matrix-matrix zero matrix", lambda: (
        res := Matrix([[1.0, 2.0], [3.0, 4.0]]).mul_mat(Matrix([[0.0, 0.0], [0.0, 0.0]])),
        res.print(),
        print("OK" if res.data == [[0.0, 0.0], [0.0, 0.0]] else "KO")
    ))

    test("Matrix-matrix incompatible size", lambda: (
        Matrix([[1.0, 2.0]]).mul_mat(Matrix([[1.0, 2.0]])).print()
    ))


if __name__ == "__main__":
    main()
