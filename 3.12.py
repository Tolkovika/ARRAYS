array = [2, 3, 2, 5, 8, 1, 9, 8]
# wybieram liczby ktore pojawiaja sie tylko raz
unique = [num for num in array if array.count(num) == 1]
print(f"Raz powtzrzajace sie liczby: {unique}")
