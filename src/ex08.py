from matrix import Matrix
from ex00 import test


def main():
    # trace (subject examples)
    test("Trace identity 2x2", lambda: (
        res := Matrix([
            [1.0, 0.0],
            [0.0, 1.0]
        ]).trace(),
        print(res),
        print("OK" if res == 2.0 else "KO")
    ))

    test("Trace subject 3x3 #1", lambda: (
        res := Matrix([
            [2.0, -5.0, 0.0],
            [4.0, 3.0, 7.0],
            [-2.0, 3.0, 4.0]
        ]).trace(),
        print(res),
        print("OK" if res == 9.0 else "KO")
    ))

    test("Trace subject 3x3 #2", lambda: (
        res := Matrix([
            [-2.0, -8.0, 4.0],
            [1.0, -23.0, 4.0],
            [0.0, 6.0, 4.0]
        ]).trace(),
        print(res),
        print("OK" if res == -21.0 else "KO")
    ))

    # extra
    test("Trace 1x1", lambda: (
        res := Matrix([[42.0]]).trace(),
        print(res),
        print("OK" if res == 42.0 else "KO")
    ))

    test("Trace zero matrix", lambda: (
        res := Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).trace(),
        print(res),
        print("OK" if res == 0.0 else "KO")
    ))

    test("Trace with negatives", lambda: (
        res := Matrix([
            [-1.0, 2.0],
            [3.0, -4.0]
        ]).trace(),
        print(res),
        print("OK" if res == -5.0 else "KO")
    ))

    # errors
    test("Trace non-square matrix", lambda: (
        Matrix([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]).trace()
    ))


if __name__ == "__main__":
    main()
