from vector import Vector
from matrix import Matrix

def test(name, fn):
    try:
        print(f"\n--- {name} ---")
        fn()
    except Exception as e:
        print(f"Error: {e}")

def main():

    # vector (subject examples)

    test("Vector add (subject)", lambda: (
        (u := Vector([2.0, 3.0])),
        (v := Vector([5.0, 7.0])),
        u.add(v),
        u.print()
    ))
    # expected: [7.0, 10.0]

    test("Vector sub (subject)", lambda: (
        (u := Vector([2.0, 3.0])),
        (v := Vector([5.0, 7.0])),
        u.sub(v),
        u.print()
    ))
    # expected: [-3.0, -4.0]

    test("Vector scl (subject)", lambda: (
        (u := Vector([2.0, 3.0])),
        u.scl(2.0),
        u.print()
    ))
    # expected: [4.0, 6.0]

    # matrix (subject examples)

    test("Matrix add (subject)", lambda: (
        (u := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (v := Matrix([[7.0, 4.0], [-2.0, 2.0]])),
        u.add(v),
        u.print()
    ))
    # expected:
    # [8.0, 6.0]
    # [1.0, 6.0]

    test("Matrix sub (subject)", lambda: (
        (u := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        (v := Matrix([[7.0, 4.0], [-2.0, 2.0]])),
        u.sub(v),
        u.print()
    ))
    # expected:
    # [-6.0, -2.0]
    # [5.0, 2.0]

    test("Matrix scl (subject)", lambda: (
        (u := Matrix([[1.0, 2.0], [3.0, 4.0]])),
        u.scl(2.0),
        u.print()
    ))
    # expected:
    # [2.0, 4.0]
    # [6.0, 8.0]

    # edges

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
