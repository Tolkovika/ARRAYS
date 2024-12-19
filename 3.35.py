def transpose_matrix(m):
    return list(map(list, zip(*m)))

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7],
    [8, 9, 0],
    [1, 2, 3]
]

print("Transposed matrix1:")
for row in transpose_matrix(matrix1):
    print(row)

print("\nTransposed matrix2:")
for row in transpose_matrix(matrix2):
    print(row)

print("\nTransposed matrix3:")
for row in transpose_matrix(matrix3):
    print(row)
