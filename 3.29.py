def create_2d_arr(x, y):
    return [[0] * y for _ in range(x)]

#  3x5 array
array = create_2d_arr(3, 5)
for row in array:
    print(row)

