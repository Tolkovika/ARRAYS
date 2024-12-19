def second_largest(array):
    largest = max(array)
    return max([x for x in array if x != largest])

def difference(array):
    return max(array) - min(array)

def median(array):
    sorted_array = sorted(array)
    mid = len(sorted_array) // 2
    return sorted_array[mid] if len(array) % 2 else (sorted_array[mid-1] + sorted_array[mid]) / 2

def min_max(array):
    return [min(array), max(array)]

def as_string(array):
    return '-'.join(map(str, array))

array = [7, 3, 8, 5, 2]
print("Druga największa liczba:", second_largest(array))
print("Różnica:", difference(array))
print("Mediana:", median(array))
print("Min i Max:", min_max(array))
print("Tablica jako string:", as_string(array))
