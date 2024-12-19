array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_val = float('inf')
max_val = float('-inf')
min_pos = None
max_pos = None

for i, row in enumerate(array):
    for j, value in enumerate(row):
        if value < min_val:
            min_val = value
            min_pos = (i, j)
        if value > max_val:
            max_val = value
            max_pos = (i, j)

print("Smallest value:", min_val, "at position:", min_pos)
print("Largest value:", max_val, "at position:", max_pos)
