def create_box(m, n):
    A = [[1] * m for i in range(n)]
    for i in range(m//2):
        for j in range(n//2):
            A[i][j] = j + 1
    print(A)


create_box(7, 7)