from matrix import Matrix
from ex00 import test


def main():
    # subject examples
    test("Subject Rank identity 3x3", lambda: print(
        Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).rank()
    ))
    # expected: 3

    test("Subject Rank dependent rows 3x4", lambda: print(
        Matrix([
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0]
        ]).rank()
    ))
    # expected: 2

    test("Subject Rank subject 4x3", lambda: print(
        Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0]
        ]).rank()
    ))
    # expected: 3

    # edge cases

    test("Rank zero matrix", lambda: print(
        Matrix([
            [0.0, 0.0],
            [0.0, 0.0]
        ]).rank()
    ))
    # expected: 0

    test("Rank 1x1 non-zero", lambda: print(
        Matrix([[42.0]]).rank()
    ))
    # expected: 1

    test("Rank 1x1 zero", lambda: print(
        Matrix([[0.0]]).rank()
    ))
    # expected: 0

    test("Rank rectangular full rank", lambda: print(
        Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ]).rank()
    ))
    # expected: 2

    test("Rank rectangular with dependent rows", lambda: print(
        Matrix([
            [1.0, 2.0],
            [2.0, 4.0],
            [3.0, 6.0]
        ]).rank()
    ))
    # expected: 1


if __name__ == "__main__":
    main()
