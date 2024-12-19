array = [-15, 8, -31, 47, -2, 19]

# ustawiamy maksymalną i minimalną wartość na pierwszy element tablicy
max_num = array[0]
min_num = array[0]

# szukamy maksymalną i minimalną wartość
for num in array:
    if num > max_num:  # jesli num jest większy od maksymalnej wartości
        max_num = num  
    if num < min_num:  # jesli num jest mniejszy od minimalnej wartości
        min_num = num  

print("Największa liczba:", max_num)
print("Najmniejsza liczba:", min_num)
