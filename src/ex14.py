from projection import projection
import os


def write_proj(matrix, path="src/matrix_display/proj"):
    with open(path, "w") as f:
        for row in matrix.data:
            line = ", ".join(str(float(x)) for x in row)
            f.write(line + "\n")


def main():
    p = projection(
        fov=90.0,
        ratio=1.0,
        near=1.0,
        far=100.0
    )

    write_proj(p)

    os.chdir("src/matrix_display")
    os.system("WAYLAND_DISPLAY= ./display")


if __name__ == "__main__":
    main()
