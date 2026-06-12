from vector import Vector
from matrix import Matrix
from ex00 import test


def main():
    # mul_vec
    test("Matrix-vector 2x2", lambda: (
        (m := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (v := Vector([5.0, 6.0])),
        m.mul_vec(v).print()
    ))  # [17, 39]

    test("Matrix-vector identity", lambda: (
        (m := Matrix([[1.0, 0.0], [0.0, 1.0]])),
        (v := Vector([42.0, 21.0])),
        m.mul_vec(v).print()
    ))  # [42, 21]

    test("Matrix-vector zero matrix", lambda: (
        (m := Matrix([[0.0, 0.0], [0.0, 0.0]])),
        (v := Vector([5.0, 6.0])),
        m.mul_vec(v).print()
    ))  # [0, 0]

    test("Matrix-vector incompatible size", lambda: (
        (m := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (v := Vector([1.0, 2.0, 3.0])),
        m.mul_vec(v).print()
    ))

    # mul_mat
    test("Matrix-matrix 2x2", lambda: (
        (m1 := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (m2 := Matrix([[5.0, 6.0], [7.0, 8.0]])),
        m1.mul_mat(m2).print()
    ))
    # [[19, 22],
    #  [43, 50]]

    test("Matrix-matrix identity", lambda: (
        (m1 := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (m2 := Matrix([[1.0, 0.0], [0.0, 1.0]])),
        m1.mul_mat(m2).print()
    ))
    # [[1, 2],
    #  [3, 4]]

    test("Matrix-matrix rectangular", lambda: (
        (m1 := Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ])),
        (m2 := Matrix([
            [7.0, 8.0],
            [9.0, 10.0],
            [11.0, 12.0]
        ])),
        m1.mul_mat(m2).print()
    ))
    # [[58, 64],
    #  [139, 154]]

    test("Matrix-matrix zero matrix", lambda: (
        (m1 := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (m2 := Matrix([[0.0, 0.0], [0.0, 0.0]])),
        m1.mul_mat(m2).print()
    ))
    # [[0, 0],
    #  [0, 0]]

    test("Matrix-matrix incompatible size", lambda: (
        (m1 := Matrix([[1.0, 2.0]])),
        (m2 := Matrix([[1.0, 2.0]])),
        m1.mul_mat(m2).print()
    ))


if __name__ == "__main__":
    main()
