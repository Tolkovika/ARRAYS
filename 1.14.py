def bubbleSort(arr):
    n = len(arr)  # Określamy długość listy arr
    for i in range(n-1):  # Zewnętrzna pętla: wykonujemy n-1 przejść po liście
        for j in range(n-i-1):  # Wewnętrzna pętla: przeglądamy elementy przed ostatnim i-tym
            if arr[j] > arr[j+1]:  # Jeśli element j jest większy od elementu j+1
                # Zamieniamy miejscami elementy arr[j] i arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Zwracamy posortowaną listę
