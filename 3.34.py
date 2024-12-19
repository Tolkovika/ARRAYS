def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

#  3x3, 5x5,8x8 identycz macierze
for size in [3, 5, 8]:
    print(f"Identity matrix of size {size}:")
    matrix = identity_matrix(size)
    for row in matrix:
        print(row)
    print()