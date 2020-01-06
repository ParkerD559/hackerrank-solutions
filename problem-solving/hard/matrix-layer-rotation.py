"""
Notes:
[
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], -> [2, 3, ... 12, 1]
    [1, 2, 3, 4] -> [2, 3, 4, 1]
]

<-------------------->  <-------------------->  <-------------------->  <-------------------->
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1)
<---->  <---->  <---->  <---->
(1, 1), (2, 1), (2, 2), (1, 2)


"""


def iter_shell(m, n, s):
    """Returns coordinates in clockwise order of shell s in m x n matrix"""
    left_column = top_row = s
    right_column = n - s - 1
    bottom_row = m - s - 1

    for column in range(left_column, right_column):
        yield (column, top_row)  # Top
    for row in range(top_row, bottom_row):
        yield (right_column, row)  # Right
    for column in range(right_column, left_column, -1):
        yield (column, bottom_row)  # Bottom
    for row in range(bottom_row, top_row, -1):
        yield (left_column, row)  # Left


def rotate(shell, r):
    rotations = r % len(shell)
    return shell[rotations:] + shell[:rotations]


def matrix_rotation(matrix, m, n, r):
    num_shells = min(m, n) // 2
    shells = [
        [matrix[y][x] for x, y in iter_shell(m, n, num)] for num in range(num_shells)
    ]
    rotated = [rotate(shell, r) for shell in shells]
    for s, shell in enumerate(rotated):
        for (x, y), val in zip(iter_shell(m, n, s), shell):
            matrix[y][x] = val


if __name__ == "__main__":
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrix_rotation(matrix, m, n, r)

    for row in matrix:
        print(" ".join(map(str, row)))
