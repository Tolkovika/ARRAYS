import random

# funkcja do losowego wybierania elementu z array
def rand_elem(array):
    return random.choice(array)

arr = [1, 2, 3, 4, 5, 6]

print("Losowy element 1:", rand_elem(arr))
print("Losowy element 2:", rand_elem(arr))
print("Losowy element 3:", rand_elem(arr))