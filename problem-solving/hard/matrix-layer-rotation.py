"""
Notes:
[
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], -> [2, 3, ... 12, 1]
    [1, 2, 3, 4] -> [2, 3, 4, 1]
]

<----------------------- up ------------------------->  <---------------- down -------------->
(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1)
<-------------------->  <---->
(1, 1), (2, 1), (2, 2), (1, 2)


"""


def matrixShells(matrix, m, n):
    """Returns shells of matrix in clockwise rotation"""
    num_shells = min(m, n) / 2
    return [
        [num[y, x] for x in range(i, n - i) for y in range()] for i in range(num_shells)
    ]


def matrixRotation(matrix, m, n, r):
    pass
