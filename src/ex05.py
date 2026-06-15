from vector import Vector
from linear_algebra import angle_cos
from ex00 import test


def main():
    # angle cosine
    test("Angle cosine identical vectors", lambda: print(
        angle_cos(
            Vector([1.0, 0.0]),
            Vector([1.0, 0.0])
        )
    ))  # 1

    test("Angle cosine orthogonal vectors", lambda: print(
        angle_cos(
            Vector([1.0, 0.0]),
            Vector([0.0, 1.0])
        )
    ))  # 0

    test("Angle cosine opposite vectors", lambda: print(
        angle_cos(
            Vector([1.0, 0.0]),
            Vector([-1.0, 0.0])
        )
    ))  # -1

    test("Angle cosine subject example 1", lambda: print(
        angle_cos(
            Vector([1.0, 0.0]),
            Vector([1.0, 0.0])
        )
    ))  # 1

    test("Angle cosine subject example 2", lambda: print(
        angle_cos(
            Vector([1.0, 0.0]),
            Vector([0.0, 1.0])
        )
    ))  # 0

    test("Angle cosine subject example 3", lambda: print(
        angle_cos(
            Vector([-1.0, 1.0]),
            Vector([1.0, -1.0])
        )
    ))  # -1

    test("Angle cosine subject example 4", lambda: print(
        angle_cos(
            Vector([1, 2, 3]),
            Vector([4, 5, 6])
        )
    ))  # -1

    test("Angle cosine arbitrary vectors", lambda: print(
        angle_cos(
            Vector([2.0, 1.0]),
            Vector([4.0, 2.0])
        )
    ))  # 0.9746

    # edges, errors
    test("Angle cosine size mismatch", lambda: print(
        angle_cos(
            Vector([1.0, 2.0]),
            Vector([1.0, 2.0, 3.0])
        )
    ))

    test("Angle cosine type mismatch", lambda: print(
        angle_cos(
            Vector([1, 2, 3]),
            Vector([1.0, 2.0, 3.0])
        )
    ))

    test("Angle cosine zero vector", lambda: print(
        angle_cos(
            Vector([0.0, 0.0]),
            Vector([1.0, 1.0])
        )
    ))


if __name__ == "__main__":
    main()
