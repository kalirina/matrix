from vector import Vector
from ex00 import test


def main():

    # norm 1
    test("Norm_1 basic 2D", lambda: print(
        Vector([1.0, -2.0, 3.0]).norm_1()
    ))  # 6
    test("Norm_1 with negatives", lambda: print(
        Vector([-1.0, -2.0, -3.0]).norm_1()
    ))  # 6
    test("Norm_1 zero vector", lambda: print(
        Vector([0.0, 0.0, 0.0]).norm_1()
    ))  # 0

    # norm
    test("Norm basic 2D", lambda: print(
        Vector([3.0, 4.0]).norm()
    ))  # 5
    test("Norm 3D", lambda: print(
        Vector([1.0, 2.0, 2.0]).norm()
    ))  # 3
    test("Norm zero vector", lambda: print(
        Vector([0.0, 0.0, 0.0]).norm()
    ))  # 0

    # norm_inf
    test("Norm inf basic", lambda: print(
        Vector([1.0, -2.0, 3.0]).norm_inf()
    ))  # 3
    test("Norm inf all negative", lambda: print(
        Vector([-1.0, -5.0, -3.0]).norm_inf()
    ))  # 5
    test("Norm inf single value", lambda: print(
        Vector([42.0]).norm_inf()
    ))  # 42

    # edges, errors
    test("Norm empty vector", lambda: Vector([]))
    test("Norm mixed types", lambda: Vector([1, 2.0, 3]))


if __name__ == "__main__":
    main()
