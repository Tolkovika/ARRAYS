def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Testowanie z trzema tablicami
arrays = [[7, 3, 9, 2], [10, 1, 5, 6], [12, 4, 11, 8]]
for arr in arrays:
    print("Pierwotna:", arr)
    print("Posortowana:", bubblesort(arr))
