from vector import Vector
from linear_algebra import linear_combination
from ex00 import test


def main():
    test("Subject example #1", lambda: (
        res := linear_combination(
            [Vector([1., 0., 0.]), Vector([0., 1., 0.]), Vector([0., 0., 1.])],
            [10., -2., 0.5]
        ),
        res.print(),
        print("OK" if res.data == [10., -2., 0.5] else "KO")
    ))

    test("Subject example #2", lambda: (
        res := linear_combination(
            [Vector([1., 2., 3.]), Vector([0., 10., -100.])],
            [10., -2.]
        ),
        res.print(),
        print("OK" if res.data == [10., 0., 230.] else "KO")
    ))

    test("Single vector", lambda: (
        res := linear_combination(
            [Vector([1., 2., 3.])],
            [5.]
        ),
        res.print(),
        print("OK" if res.data == [5., 10., 15.] else "KO")
    ))

    test("Zero coefficients", lambda: (
        res := linear_combination(
            [Vector([1., 2., 3.]), Vector([4., 5., 6.])],
            [0., 0.]
        ),
        res.print(),
        print("OK" if res.data == [0., 0., 0.] else "KO")
    ))

    test("Empty vectors list", lambda: (
        linear_combination([], [1.])
    ))

    test("Empty coefficients list", lambda: (
        linear_combination([Vector([1., 2., 3.])], [])
    ))

    test("Different number of vectors and coefficients", lambda: (
        linear_combination(
            [Vector([1., 2., 3.]), Vector([4., 5., 6.])],
            [1.]
        )
    ))

    test("Vectors of different sizes", lambda: (
        linear_combination(
            [Vector([1., 2., 3.]), Vector([4., 5.])],
            [1., 2.]
        )
    ))


if __name__ == "__main__":
    main()
