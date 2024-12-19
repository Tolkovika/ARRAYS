array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# f liczby, które są w array1, ale nie ma ich w array2
result = [num for num in array1 if num not in array2]
print("Liczby w pierwszej tablicy, ale nie w drugiej:", result)

