array = [15, 8, 31, 47, 2, 19]

# inicjalizujemy zmienną do przechowywania sumy
suma = 0

# obliczamy sume elementów tablicy
for num in array:
    suma += num  

# obliczamy s.a.
srednia = suma / len(array)

print(array)
print(f"Średnia arytmetyczna: {srednia}")
