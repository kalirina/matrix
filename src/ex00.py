from vector import Vector
from matrix import Matrix

def test(name, fn):
    try:
        print(f"\n--- {name} ---")
        fn()
    except Exception as e:
        print(f"Error: {e}")

def main():

    # vectors

    test("Vector add", lambda: (
        (v1 := Vector([1, 2, 3])),
        v1.add(Vector([4, 5, 6])),
        v1.print()
    ))

    test("Vector sub", lambda: (
        (v1 := Vector([5, 7, 9])),
        v1.sub(Vector([1, 2, 3])),
        v1.print()
    ))

    test("Vector scl", lambda: (
        (v1 := Vector([1, 2, 3])),
        v1.scl(3),
        v1.print()
    ))

    test("Vector empty", lambda: Vector([]))

    test("Vector mixed types", lambda: Vector([1, 2.0, 3]))

    test("Vector size mismatch", lambda: (
        (v1 := Vector([1, 2, 3])),
        v1.add(Vector([1, 2]))
    ))

    test("Vector type mismatch", lambda: (
        (v1 := Vector([1, 2, 3])),
        v1.add(Vector([1.0, 2.0, 3.0]))
    ))

    # matrices

    test("Matrix add", lambda: (
        (m1 := Matrix([[1, 2], [3, 4]])),
        m1.add(Matrix([[5, 6], [7, 8]])),
        m1.print()
    ))

    test("Matrix sub", lambda: (
        (m1 := Matrix([[5, 6], [7, 8]])),
        m1.sub(Matrix([[1, 2], [3, 4]])),
        m1.print()
    ))

    test("Matrix scl", lambda: (
        (m1 := Matrix([[1, 2], [3, 4]])),
        m1.scl(2),
        m1.print()
    ))

    test("Matrix empty", lambda: Matrix([]))

    test("Matrix irregular", lambda: Matrix([
        [1, 2],
        [3]
    ]))

    test("Matrix size mismatch", lambda: (
        (m1 := Matrix([[1, 2], [3, 4]])),
        m1.add(Matrix([[1, 2, 3], [4, 5, 6]]))
    ))

    test("Matrix type mismatch", lambda: (
        (m1 := Matrix([[1, 2], [3, 4]])),
        m1.add(Matrix([[1.0, 2.0], [3.0, 4.0]]))
    ))

if __name__ == "__main__":
    main()
