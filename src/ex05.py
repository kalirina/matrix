from vector import Vector
from linear_algebra import angle_cos
from ex00 import test


def main():
    # angle cosine
    test("Angle cosine identical vectors", lambda: (
        res := angle_cos(Vector([1.0, 0.0]), Vector([1.0, 0.0])),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))

    test("Angle cosine orthogonal vectors", lambda: (
        res := angle_cos(Vector([1.0, 0.0]), Vector([0.0, 1.0])),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Angle cosine opposite vectors", lambda: (
        res := angle_cos(Vector([1.0, 0.0]), Vector([-1.0, 0.0])),
        print(res),
        print("OK" if res == -1.0 else "KO")
    ))

    test("Angle cosine subject example 1", lambda: (
        res := angle_cos(Vector([1.0, 0.0]), Vector([1.0, 0.0])),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))

    test("Angle cosine subject example 2", lambda: (
        res := angle_cos(Vector([1.0, 0.0]), Vector([0.0, 1.0])),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Angle cosine subject example 3", lambda: (
        res := angle_cos(Vector([-1.0, 1.0]), Vector([1.0, -1.0])),
        print(res),
        print("OK" if res == -1.0 else "KO")
    ))

    test("Angle cosine subject example 4", lambda: (
        res := angle_cos(Vector([1, 2, 3]), Vector([4, 5, 6])),
        print(res),
        print("OK" if abs(res - 0.974631846) < 1e-6 else "KO")
    ))

    test("Angle cosine arbitrary vectors", lambda: (
        res := angle_cos(Vector([2.0, 1.0]), Vector([4.0, 2.0])),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))

    test("Angle cosine different type", lambda: (
        res := angle_cos(Vector([1, 2, 3]), Vector([1.0, 2.0, 3.0])),
        print(res),
        print("OK" if res == 1.0 else "KO")
    ))

    # edges, errors
    test("Angle cosine size mismatch", lambda: (
        angle_cos(Vector([1.0, 2.0]), Vector([1.0, 2.0, 3.0]))
    ))

    test("Angle cosine zero vector", lambda: (
        angle_cos(Vector([0.0, 0.0]), Vector([1.0, 1.0]))
    ))


if __name__ == "__main__":
    main()
