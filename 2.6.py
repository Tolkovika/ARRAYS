matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# zmieniamy elementy na głównej przekątnej na 1
for i in range(len(matrix)):  # dla każdego wiersza w macierzy
    matrix[i][i] = 1  # wartość przekątnej 1

# modyfikacja macierzy
for row in matrix:
    print(" ".join(str(item) for item in row))  # laczymy elementy wiersza w jeden ciąg oddzielony spacją
