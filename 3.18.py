import myarrays_3_18  

array = [7, 3, 8, 5, 2]
print("Array:", ','.join(map(str, array)))

# Druga największa liczba
second_largest_number = myarrays_3_18.second_largest(array)
print("Druga największa liczba:", second_largest_number)

# Mediana
median_value = myarrays_3_18.median(array)
print("Mediana:", median_value)

# Najmniejsza i największa liczba
smallest, largest = myarrays_3_18.min_max(array)
print("Najmniejsza i największa liczba:", smallest, largest)

# Liczby jako ciąg znaków
array_as_string = myarrays_3_18.as_string(array)
print("Liczby jako ciąg znaków:", array_as_string)