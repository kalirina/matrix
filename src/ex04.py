from vector import Vector
from ex00 import test


def main():

    # norm (subject examples)
    test("Norm subject 0", lambda: (
        v := Vector([0.0, 0.0, 0.0]),
        res1 := v.norm_1(),
        res2 := v.norm(),
        res3 := v.norm_inf(),
        print(res1, res2, res3),
        print("OK" if (res1, res2, res3) == (0.0, 0.0, 0.0) else "KO")
    ))

    test("Norm subject 1", lambda: (
        v := Vector([1.0, 2.0, 3.0]),
        res1 := v.norm_1(),
        res2 := v.norm(),
        res3 := v.norm_inf(),
        print(res1, res2, res3),
        print("OK" if (res1, res2, res3) == (6.0, 3.7416573867739413, 3.0) else "KO")
    ))

    test("Norm subject 2", lambda: (
        v := Vector([-1.0, -2.0]),
        res1 := v.norm_1(),
        res2 := v.norm(),
        res3 := v.norm_inf(),
        print(res1, res2, res3),
        print("OK" if (res1, res2, res3) == (3.0, 2.23606797749979, 2.0) else "KO")
    ))

    # norm 1
    test("Norm_1 basic 2D", lambda: (
        res := Vector([1.0, -2.0, 3.0]).norm_1(),
        print(res),
        print("OK" if res == 6.0 else "KO")
    ))

    test("Norm_1 with negatives", lambda: (
        res := Vector([-1.0, -2.0, -3.0]).norm_1(),
        print(res),
        print("OK" if res == 6.0 else "KO")
    ))

    test("Norm_1 zero vector", lambda: (
        res := Vector([0.0, 0.0, 0.0]).norm_1(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    # norm
    test("Norm basic 2D", lambda: (
        res := Vector([3.0, 4.0]).norm(),
        print(res),
        print("OK" if res == 5.0 else "KO")
    ))

    test("Norm 3D", lambda: (
        res := Vector([1.0, 2.0, 2.0]).norm(),
        print(res),
        print("OK" if res == 3.0 else "KO")
    ))

    test("Norm zero vector", lambda: (
        res := Vector([0.0, 0.0, 0.0]).norm(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    # norm_inf
    test("Norm inf basic", lambda: (
        res := Vector([1.0, -2.0, 3.0]).norm_inf(),
        print(res),
        print("OK" if res == 3.0 else "KO")
    ))

    test("Norm inf all negative", lambda: (
        res := Vector([-1.0, -5.0, -3.0]).norm_inf(),
        print(res),
        print("OK" if res == 5.0 else "KO")
    ))

    test("Norm inf single value", lambda: (
        res := Vector([42.0]).norm_inf(),
        print(res),
        print("OK" if res == 42.0 else "KO")
    ))

    # edges, errors
    test("Norm empty vector", lambda: Vector([]))

    test("Norm mixed types", lambda: Vector([1, 2.0, 3]))


if __name__ == "__main__":
    main()
