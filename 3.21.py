arr1 = [6, 4, 2]
arr2 = [2, 4, 6, 7, 8, 9]

arr1jest_arr2 = True  # zakładamy, że arr1 jest podzbiorem arr2

for number in arr1:
    if number not in arr2:
        arr1jest_arr2 = False  # Jeśli któryś element nie jest w arr2, to arr1 nie jest podzbiorem arr2
        break  #  przerywamy pętlę

if arr1jest_arr2:
    print("arr1 jest podzbiorem arr2")
else:
    print("arr1 nie jest podzbiorem arr2")




