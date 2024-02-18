"""Given two positive integers m (width) and n (height), fill a two-dimensional list
(or array) of size m-by-n in the following way:

(1) All the elements in the first and last row and column are 1.

(2) All the elements in the second and second-last row and column are 2,
excluding the elements from step 1.

(3) All the elements in the third and third-last row and column are 3,
excluding the elements from the previous steps.

And so on ...

Examples
Given m = 5, n = 8, your function should return

[[1, 1, 1, 1, 1],
 [1, 2, 2, 2, 1],
 [1, 2, 3, 2, 1],
 [1, 2, 3, 2, 1],
 [1, 2, 3, 2, 1],
 [1, 2, 3, 2, 1],
 [1, 2, 2, 2, 1],
 [1, 1, 1, 1, 1]]
Given m = 10, n = 9, your function should return

[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
 [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
 [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
 [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
 [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]"""


def create_box(m, n):
    A = [[1] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i < (n // 2):
                i1 = i
            else:
                i1 = n - i - 1
            if j < (m // 2):
                j1 = j
            else:
                j1 = m - j - 1
            A[i][j] = min(i1, j1) + 1
    return A