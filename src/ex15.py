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
    ))

    test("Vector sub: complex - complex", lambda: (
        (v1 := Vector([Complex(5, 6), Complex(7, 8)])),
        v1.sub(Vector([Complex(1, 2), Complex(3, 4)])),
        v1.print()
    ))

    test("Vector scl: complex * float/int", lambda: (
        (v1 := Vector([Complex(1, 2), Complex(3, 4)])),
        v1.scl(2),
        v1.print()
    ))

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
    ))

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
    ))

    test("Matrix scl: complex * complex", lambda: (
        (m1 := Matrix([
            [Complex(1, 1), Complex(2, 2)],
            [Complex(3, 3), Complex(4, 4)]
        ])),
        m1.scl(Complex(2, 0)),
        m1.print()
    ))

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
    ))

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
    ))

    print("\n------- EX03 ------")

    test("Dot product", lambda: print(
        Vector([Complex(1, 1), Complex(2, 2)]).dot(
            Vector([Complex(3, 3), Complex(4, 4)])
        )
    ))

    print("\n------- EX04 ------")

    test("Norm", lambda: print(
        Vector([Complex(3, 0), Complex(4, 0)]).norm_1(),
        Vector([Complex(3, 0), Complex(4, 0)]).norm(),
        Vector([Complex(3, 0), Complex(4, 0)]).norm_inf()
    ))

    print("\n------- EX05 ------")

    test("Angle cosine complex identical", lambda: print(
        angle_cos(
            Vector([Complex(1, 0), Complex(2, 0)]),
            Vector([Complex(1, 0), Complex(2, 0)])
        )
    ))

    test("Angle cosine complex and float/int", lambda: print(
        angle_cos(
            Vector([Complex(-1, 0), Complex(1, 0)]),
            Vector([1, -1])
        )
    ))

    print("\n------- EX06 ------")

    test("Cross product complex", lambda: print(
        cross_product(
            Vector([Complex(1, 2), Complex(0, 1), Complex(3, -1)]),
            Vector([Complex(4, -1), Complex(1, 0), Complex(2, 2)])
        )
    ))

    test("Cross product complex and float/int", lambda: print(
        cross_product(
            Vector([Complex(1, 2), Complex(0, 1), Complex(3, -1)]),
            Vector([1.0, 2.0, 3.0])
        )
    ))

    print("\n------- EX07 ------")

    test("Matrix mul vec complex", lambda: (
        Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ]).mul_vec(Vector([Complex(5, 6), Complex(7, 8)])).print()
    ))

    test("Matrix mul mat complex", lambda: (
        Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ]).mul_mat(Matrix([
            [Complex(1, 0), Complex(2, 0)],
            [Complex(3, 0), Complex(4, 0)]
        ])).print()
    ))

    print("\n------- EX08 ------")

    test("Trace complex", lambda: print(
        Matrix([
            [Complex(1, 1), Complex(0, 0)],
            [Complex(0, 0), Complex(2, 2)]
        ]).trace()
    ))

    print("\n------- EX09 ------")

    test("Transpose complex 3x3", lambda: (
        Matrix([
            [Complex(1, 1), Complex(2, -1), Complex(3, 0)],
            [Complex(4, 2), Complex(5, 0), Complex(6, -3)],
            [Complex(7, -1), Complex(8, 1), Complex(9, 2)]
        ]).transpose().print()
    ))

    print("\n------- EX10 ------")

    test("Row echelon complex 3x3", lambda: (
        Matrix([
            [Complex(1, 1), Complex(2, 0), Complex(3, -1)],
            [Complex(2, 2), Complex(4, 0), Complex(6, -2)],
            [Complex(1, 0), Complex(0, 1), Complex(1, 1)]
        ]).row_echelon().print()
    ))


    # test("Determinant complex", lambda: print(
    #     Matrix([
    #         [Complex(1, 0), Complex(2, 0)],
    #         [Complex(3, 0), Complex(4, 0)]
    #     ]).determinant()
    # ))


    # # inverse
    # test("Inverse complex", lambda: (
    #     Matrix([
    #         [Complex(1, 0), Complex(0, 0)],
    #         [Complex(0, 0), Complex(1, 0)]
    #     ]).inverse().print()
    # ))


if __name__ == "__main__":
    main()
