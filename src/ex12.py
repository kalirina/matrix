from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Subject Inverse identity 3x3", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).inverse(),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ] else "KO")
    ))

    test("Subject Inverse diagonal 3x3", lambda: (
        res := Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ]).inverse(),
        res.print(),
        print("OK" if res.data == [
            [0.5, 0.0, 0.0],
            [0.0, 0.5, 0.0],
            [0.0, 0.0, 0.5]
        ] else "KO")
    ))

    test("Subject Inverse subject 3x3", lambda: (
        res := Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ]).inverse(),
        res.print(),
        print("OK" if all(
            abs(res.data[i][j] - expected) < 1e-6
            for i, row in enumerate([
                [0.649425287, 0.097701149, -0.655172414],
                [-0.781609195, -0.126436782, 0.965517241],
                [0.143678161, 0.074712644, -0.206896552]
            ])
            for j, expected in enumerate(row)
        ) else "KO")
    ))

    # edge cases

    test("Inverse 1x1", lambda: (
        res := Matrix([[5.0]]).inverse(),
        res.print(),
        print("OK" if res.data == [[0.2]] else "KO")
    ))

    test("Inverse 2x2", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]).inverse(),
        res.print(),
        print("OK" if res.data == [
            [-2.0, 1.0],
            [1.5, -0.5]
        ] else "KO")
    ))

    test("Inverse singular matrix", lambda: (
        Matrix([
            [1.0, 2.0],
            [2.0, 4.0]
        ]).inverse().print()
    ))

    test("Inverse non-square matrix", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).inverse().print()
    ))

    test("A * A^-1 = I", lambda: (
        m := Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ]),
        res := m.mul_mat(m.inverse()),
        res.print(),
        print("OK" if res.data == [
            [1.0, 0.0],
            [0.0, 1.0]
        ] else "KO")
    ))


if __name__ == "__main__":
    main()
