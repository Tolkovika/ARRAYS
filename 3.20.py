arr = [7, 9, 2, 4, 5, 6]

# array jeden dla liczb parzystych, drugi dla liczb nieparzystych
even_numbers = [x for x in arr if x % 2 == 0]
odd_numbers = [x for x in arr if x % 2 != 0]

# parzyste na początku, nieparzyste na końcu
arr = even_numbers + odd_numbers

print(f"Tablica po oddzieleniu parzystych i nieparzystych: {arr}")

