array = [15, 8, 31, 47, 2, 19]

# inicjalizujemy sume i indeks
suma = 0
indeks = 0

while indeks < len(array):
    suma += array[indeks]  # dodajemy liczby z tablicy do sumy
    indeks += 1  # przechodzimy do następnego elementu

# s.a
srednia = suma / len(array)

print(array)
print(f"Średnia arytmetyczna:{srednia}")
