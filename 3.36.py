def flatten_2d_array(arr): #Flatten splaszczony , czyli konwert z dwu w jedno wymiar
    return [item for sublist in arr for item in sublist]

array1 = [[5, 6], [7, 8]]
array2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
array3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

print("Flattened array1:", flatten_2d_array(array1))
print("Flattened array2:", flatten_2d_array(array2))
print("Flattened array3:", flatten_2d_array(array3))