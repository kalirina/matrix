from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Subject Inverse identity 3x3", lambda: (
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).inverse().print()
    ))
    # expected:
    # [1.0, 0.0, 0.0]
    # [0.0, 1.0, 0.0]
    # [0.0, 0.0, 1.0]

    test("Subject Inverse diagonal 3x3", lambda: (
        Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ]).inverse().print()
    ))
    # expected:
    # [0.5, 0.0, 0.0]
    # [0.0, 0.5, 0.0]
    # [0.0, 0.0, 0.5]

    test("Subject Inverse subject 3x3", lambda: (
        Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ]).inverse().print()
    ))
    # expected:
    # [0.649425287, 0.097701149, -0.655172414]
    # [-0.781609195, -0.126436782, 0.965517241]
    # [0.143678161, 0.074712644, -0.206896552]

    # edge cases

    test("Inverse 1x1", lambda: (
        Matrix([[5.0]]).inverse().print()
    ))
    # expected:
    # [0.2]

    test("Inverse 2x2", lambda: (
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).inverse().print()
    ))
    # expected:
    # [-2.0, 1.0]
    # [1.5, -0.5]

    test("Inverse singular matrix", lambda: (
        Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).inverse().print()
    ))
    # expected:
    # Error: Matrix doesn't have an inverse

    test("Inverse non-square matrix", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).inverse().print()
    ))
    # expected:
    # Error: Matrix must be square

    test("A * A^-1 = I", lambda: (
        (m := Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ])),
        m.mul_mat(m.inverse()).print()
    ))

if __name__ == "__main__":
    main()
