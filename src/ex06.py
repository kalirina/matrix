from vector import Vector
from linear_algebra import cross_product
from ex00 import test


def main():
    # cross product
    test("Cross product basis i x j", lambda: (
        cross_product(
            Vector([1.0, 0.0, 0.0]),
            Vector([0.0, 1.0, 0.0])
        ).print()
    ))  # [0, 0, 1]

    test("Cross product basis j x k", lambda: (
        cross_product(
            Vector([0.0, 1.0, 0.0]),
            Vector([0.0, 0.0, 1.0])
        ).print()
    ))  # [1, 0, 0]

    test("Cross product basis k x i", lambda: (
        cross_product(
            Vector([0.0, 0.0, 1.0]),
            Vector([1.0, 0.0, 0.0])
        ).print()
    ))  # [0, 1, 0]

    test("Cross product subject example 1", lambda: (
        cross_product(
            Vector([0.0, 0.0, 1.0]),
            Vector([1.0, 0.0, 0.0])
        ).print()
    ))  # [0, 1, 0]

    test("Cross product subject example 2", lambda: (
        cross_product(
            Vector([1.0, 2.0, 3.0]),
            Vector([4.0, 5.0, 6.0])
        ).print()
    ))  # [-3, 6, -3]

    test("Cross product identical vectors", lambda: (
        cross_product(
            Vector([1.0, 2.0, 3.0]),
            Vector([1.0, 2.0, 3.0])
        ).print()
    ))  # [0, 0, 0]

    test("Cross product parallel vectors", lambda: (
        cross_product(
            Vector([1.0, 2.0, 3.0]),
            Vector([2.0, 4.0, 6.0])
        ).print()
    ))  # [0, 0, 0]

    # edges, errors
    test("Cross product size mismatch", lambda: (
        cross_product(
            Vector([1.0, 2.0, 3.0]),
            Vector([1.0, 2.0])
        ).print()
    ))

    test("Cross product not 3D", lambda: (
        cross_product(
            Vector([1.0, 2.0]),
            Vector([3.0, 4.0])
        ).print()
    ))

    test("Cross product type mismatch", lambda: (
        cross_product(
            Vector([1, 2, 3]),
            Vector([1.0, 2.0, 3.0])
        ).print()
    ))


if __name__ == "__main__":
    main()
