from vector import Vector
from matrix import Matrix
from ex00 import test
from complex import Complex
from linear_algebra import linear_combination, lerp, angle_cos, cross_product


def main():
    print("\n------- EX00 ------")

    test("Vector add: complex + float/int", lambda: (
        (v1 := Vector([Complex(1, 2), Complex(3, 4)])),
        v1.add(Vector([3.0, 6.5])),
        v1.print()
    ))  # [4+2i, 9.5+4i]

    test("Vector sub: complex - complex", lambda: (
        (v1 := Vector([Complex(5, 6), Complex(7, 8)])),
        v1.sub(Vector([Complex(1, 2), Complex(3, 4)])),
        v1.print()
    ))  # [4+4i, 4+4i]

    test("Vector scl: complex * float/int", lambda: (
        (v1 := Vector([Complex(1, 2), Complex(3, 4)])),
        v1.scl(2),
        v1.print()
    ))  # [2+4i, 6+8i]

    test("Matrix add: complex + complex", lambda: (
        (m1 := Matrix([
            [Complex(1, 1), Complex(2, 2)],
            [Complex(3, 3), Complex(4, 4)]
        ])),
        m1.add(Matrix([
            [Complex(1, 0), Complex(1, 0)],
            [Complex(1, 0), Complex(1, 0)]
        ])),
        m1.print()
    ))  # [[2+1i, 3+2i],[4+3i, 5+4i]]

    test("Matrix sub: complex - float/int", lambda: (
        (m1 := Matrix([
            [Complex(5, 5), Complex(6, 6)],
            [Complex(7, 7), Complex(8, 8)]
        ])),
        m1.sub(Matrix([
            [1, 2],
            [3, 4]
        ])),
        m1.print()
    ))  # [[4+5i, 4+6i],[4+7i, 4+8i]]

    test("Matrix scl: complex * complex", lambda: (
        (m1 := Matrix([
            [Complex(1, 1), Complex(2, 2)],
            [Complex(3, 3), Complex(4, 4)]
        ])),
        m1.scl(Complex(2, 0)),
        m1.print()
    ))  # [[2+2i, 4+4i],[6+6i, 8+8i]]

    print("\n------- EX01 ------")

    test("Linear combination of vectors", lambda: (
        linear_combination(
            [
            Vector([Complex(1, 1), Complex(0, 0), Complex(0, 0)]),
            Vector([Complex(0, 0), Complex(1, 2), Complex(0, 0)]),
            Vector([Complex(0, 0), Complex(0, 0), Complex(2, -1)])
            ],
            [10., -2., 0.5]
        ).print()
    ))  # [10+10i, -2-4i, 1-0.5i]

    print("\n------- EX02 ------")

    test("Linear interpolation of matrices", lambda: (
        (m1 := Matrix([
            [Complex(1, 1), Complex(2, 1), Complex(3, 1)],
            [Complex(4, 1), Complex(5, 1), Complex(6, 1)],
            [Complex(7, 1), Complex(8, 1), Complex(9, 1)]
        ])),
        (m2 := Matrix([
            [9.0, 8.0, 7.0],
            [6.0, 5.0, 4.0],
            [3.0, 2.0, 1.0]
        ])),
        lerp(m1, m2, 0.5).print()
    ))  # [[5+0.5i, 5+0.5i, 5+0.5i],[5+0.5i, 5+0.5i, 5+0.5i],[5+0.5i, 5+0.5i, 5+0.5i]]

    print("\n------- EX03 ------")

    test("Dot product", lambda: print(
        Vector([Complex(1, 1), Complex(2, 2)]).dot(
            Vector([Complex(3, 3), Complex(4, 4)])
        )
    ))  # 0+22i

    print("\n------- EX04 ------")

    test("Norm", lambda: print(
        Vector([Complex(3, 0), Complex(4, 0)]).norm_1(),
        Vector([Complex(3, 0), Complex(4, 0)]).norm(),
        Vector([Complex(3, 0), Complex(4, 0)]).norm_inf()
    ))  # 7, 5, 4

    print("\n------- EX05 ------")

    test("Angle cosine complex identical", lambda: print(
        angle_cos(
            Vector([Complex(1, 0), Complex(2, 0)]),
            Vector([Complex(1, 0), Complex(2, 0)])
        )
    ))  # 1.0

    test("Angle cosine complex and float/int", lambda: print(
        angle_cos(
            Vector([Complex(-1, 0), Complex(1, 0)]),
            Vector([1, -1])
        )
    ))  # -1.0

    print("\n------- EX06 ------")

    test("Cross product complex", lambda: print(
        cross_product(
            Vector([Complex(1, 2), Complex(0, 1), Complex(3, -1)]),
            Vector([Complex(4, -1), Complex(1, 0), Complex(2, 2)])
        )
    ))  # [-5 + 3i, 13 + -13i, 0 + -2i]

    test("Cross product complex and float/int", lambda: print(
        cross_product(
            Vector([Complex(1, 2), Complex(0, 1), Complex(3, -1)]),
            Vector([1.0, 2.0, 3.0])
        )
    ))  # [-6.0 + 5.0i, 0.0 + -7.0i, 2.0 + 3.0i]

    print("\n------- EX07 ------")

    test("Matrix mul vec complex", lambda: (
        Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ]).mul_vec(Vector([Complex(5, 6), Complex(7, 8)])).print()
    ))  # [5+6i, 7+8i]

    test("Matrix mul mat complex", lambda: (
        Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ]).mul_mat(Matrix([
            [Complex(1, 0), Complex(2, 0)],
            [Complex(3, 0), Complex(4, 0)]
        ])).print()
    ))  # same matrix

    test("Matrix mul mat complex non-trivial", lambda: (
        Matrix([
            [Complex(1, 1), Complex(2, -1)],
            [Complex(0, 1), Complex(1, 0)]
        ]).mul_mat(Matrix([
            [Complex(2, 0), Complex(0, 1)],
            [Complex(1, -1), Complex(3, 0)]
        ])).print()
    ))  # [3-i, 5-2i],[1+i, 2]

    print("\n------- EX08 ------")

    test("Trace complex", lambda: print(
        Matrix([
            [Complex(1, 1), Complex(0, 0)],
            [Complex(0, 0), Complex(2, 2)]
        ]).trace()
    ))  # 3+3i

    print("\n------- EX09 ------")

    test("Transpose complex 3x3", lambda: (
        Matrix([
            [Complex(1, 1), Complex(2, -1), Complex(3, 0)],
            [Complex(4, 2), Complex(5, 0), Complex(6, -3)],
            [Complex(7, -1), Complex(8, 1), Complex(9, 2)]
        ]).transpose().print()
    ))  # transposed matrix

    print("\n------- EX10 ------")

    test("Row echelon complex 3x3", lambda: (
        Matrix([
            [Complex(1, 1), Complex(2, 0), Complex(3, -1)],
            [Complex(2, 2), Complex(4, 0), Complex(6, -2)],
            [Complex(1, 0), Complex(0, 1), Complex(1, 1)]
        ]).row_echelon().print()
    ))  # echelon form

    print("\n------- EX11 ------")

    test("Determinant complex", lambda: print(
        Matrix([
            [Complex(1, 0), Complex(2, 0)],
            [Complex(3, 0), Complex(4, 0)]
        ]).determinant()
    ))  # -2

    print("\n------- EX12 ------")

    test("Inverse complex", lambda: (
        Matrix([
            [Complex(1, 1), Complex(0, 0)],
            [Complex(0, 0), Complex(2, 0)]
        ]).inverse().print()
    )) # [[0.5-0.5i, 0], [0, 0.5]]

    print("\n------- EX13 ------")

    test("Rank complex full", lambda: (
        print(Matrix([
            [Complex(1, 1), Complex(0, 0), Complex(2, -1)],
            [Complex(0, 1), Complex(1, 1), Complex(3, 0)],
            [Complex(1, 0), Complex(2, 1), Complex(4, -1)]
        ]).rank())
    ))  # 3


if __name__ == "__main__":
    main()
