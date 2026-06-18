from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Subject Rank identity 3x3", lambda: (
        res := Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).rank(),
        print(res),
        print("OK" if res == 3 else "KO")
    ))

    test("Subject Rank dependent rows 3x4", lambda: (
        res := Matrix([
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0]
        ]).rank(),
        print(res),
        print("OK" if res == 2 else "KO")
    ))

    test("Subject Rank subject 4x3", lambda: (
        res := Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0]
        ]).rank(),
        print(res),
        print("OK" if res == 3 else "KO")
    ))

    # edge cases
    test("Rank zero matrix", lambda: (
        res := Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).rank(),
        print(res),
        print("OK" if res == 0 else "KO")
    ))

    test("Rank 1x1 non-zero", lambda: (
        res := Matrix([[42.0]]).rank(),
        print(res),
        print("OK" if res == 1 else "KO")
    ))

    test("Rank 1x1 zero", lambda: (
        res := Matrix([[0.0]]).rank(),
        print(res),
        print("OK" if res == 0 else "KO")
    ))

    test("Rank rectangular full rank", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ]).rank(),
        print(res),
        print("OK" if res == 2 else "KO")
    ))

    test("Rank rectangular with dependent rows", lambda: (
        res := Matrix([
            [1.0, 2.0],
            [2.0, 4.0],
            [3.0, 6.0]
        ]).rank(),
        print(res),
        print("OK" if res == 1 else "KO")
    ))


if __name__ == "__main__":
    main()
