from vector import Vector
from matrix import Matrix
from ex00 import test
from complex import Complex


def main():

    # vector (complex)
    test("Vector add complex", lambda: (
        (v1 := Vector([Complex(1, 2), Complex(3, 4)])),
        v1.add(Vector([Complex(5, 6), Complex(7, 8)])),
        v1.print()
    ))

    test("Vector sub complex", lambda: (
        (v1 := Vector([Complex(5, 6), Complex(7, 8)])),
        v1.sub(Vector([Complex(1, 2), Complex(3, 4)])),
        v1.print()
    ))

    test("Vector scl complex", lambda: (
        (v1 := Vector([Complex(1, 2), Complex(3, 4)])),
        v1.scl(Complex(2, 0)),
        v1.print()
    ))


    # # matrix add/sub/scl (complex)
    # test("Matrix add complex", lambda: (
    #     (m1 := Matrix([
    #         [Complex(1, 1), Complex(2, 2)],
    #         [Complex(3, 3), Complex(4, 4)]
    #     ])),
    #     m1.add(Matrix([
    #         [Complex(1, 0), Complex(1, 0)],
    #         [Complex(1, 0), Complex(1, 0)]
    #     ])),
    #     m1.print()
    # ))

    # test("Matrix sub complex", lambda: (
    #     (m1 := Matrix([
    #         [Complex(5, 5), Complex(6, 6)],
    #         [Complex(7, 7), Complex(8, 8)]
    #     ])),
    #     m1.sub(Matrix([
    #         [Complex(1, 1), Complex(2, 2)],
    #         [Complex(3, 3), Complex(4, 4)]
    #     ])),
    #     m1.print()
    # ))

    # test("Matrix scl complex", lambda: (
    #     (m1 := Matrix([
    #         [Complex(1, 1), Complex(2, 2)],
    #         [Complex(3, 3), Complex(4, 4)]
    #     ])),
    #     m1.scl(Complex(2, 0)),
    #     m1.print()
    # ))


    # # dot product
    # test("Dot complex", lambda: print(
    #     Vector([Complex(1, 1), Complex(2, 2)]).dot(
    #         Vector([Complex(3, 3), Complex(4, 4)])
    #     )
    # ))


    # # norms (must still work if implemented generically)
    # test("Norm complex", lambda: print(
    #     Vector([Complex(3, 0), Complex(4, 0)]).norm()
    # ))


    # # matrix multiplication
    # test("Matrix mul vec complex", lambda: (
    #     Matrix([
    #         [Complex(1, 0), Complex(0, 0)],
    #         [Complex(0, 0), Complex(1, 0)]
    #     ]).mul_vec(Vector([Complex(5, 6), Complex(7, 8)])).print()
    # ))

    # test("Matrix mul mat complex", lambda: (
    #     Matrix([
    #         [Complex(1, 0), Complex(0, 0)],
    #         [Complex(0, 0), Complex(1, 0)]
    #     ]).mul_mat(Matrix([
    #         [Complex(1, 0), Complex(2, 0)],
    #         [Complex(3, 0), Complex(4, 0)]
    #     ])).print()
    # ))


    # # trace
    # test("Trace complex", lambda: print(
    #     Matrix([
    #         [Complex(1, 1), Complex(0, 0)],
    #         [Complex(0, 0), Complex(2, 2)]
    #     ]).trace()
    # ))


    # # determinant
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
