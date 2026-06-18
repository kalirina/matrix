from vector import Vector
from linear_algebra import cross_product
from ex00 import test


def main():
    # cross product
    test("Cross product subject example 1", lambda: (
        res := cross_product(Vector([0.0, 0.0, 1.0]), Vector([1.0, 0.0, 0.0])),
        res.print(),
        print("OK" if res.data == [0.0, 1.0, 0.0] else "KO")
    ))

    test("Cross product subject example 2", lambda: (
        res := cross_product(Vector([1.0, 2.0, 3.0]), Vector([4.0, 5.0, 6.0])),
        res.print(),
        print("OK" if res.data == [-3.0, 6.0, -3.0] else "KO")
    ))

    test("Cross product subject example 3", lambda: (
        res := cross_product(Vector([4.0, 2.0, -3.0]), Vector([-2.0, -5.0, 16.0])),
        res.print(),
        print("OK" if res.data == [17.0, -58.0, -16.0] else "KO")
    ))

    test("Cross product identical vectors", lambda: (
        res := cross_product(Vector([1.0, 2.0, 3.0]), Vector([1.0, 2.0, 3.0])),
        res.print(),
        print("OK" if res.data == [0.0, 0.0, 0.0] else "KO")
    ))

    test("Cross product parallel vectors", lambda: (
        res := cross_product(Vector([1.0, 2.0, 3.0]), Vector([2.0, 4.0, 6.0])),
        res.print(),
        print("OK" if res.data == [0.0, 0.0, 0.0] else "KO")
    ))

    test("Cross product different types", lambda: (
        res := cross_product(Vector([1, 2, 3]), Vector([1.0, 2.0, 3.0])),
        res.print(),
        print("OK" if res.data == [0.0, 0.0, 0.0] else "KO")
    ))

    # edges, errors
    test("Cross product size mismatch", lambda: (
        cross_product(Vector([1.0, 2.0, 3.0]), Vector([1.0, 2.0])).print()
    ))

    test("Cross product not 3D", lambda: (
        cross_product(Vector([1.0, 2.0]), Vector([3.0, 4.0])).print()
    ))


if __name__ == "__main__":
    main()
