array = [[(i + 1) * (j + 1) for j in range(5)] for i in range(5)]

for row in array:
    print(' '.join(map(str, row)))
