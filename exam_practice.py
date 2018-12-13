def sum_columns(data):
    n = len(data)
    sums = [0]*n
    for col in range(n):
        for row in range(n):
            sums[col] += data[row][col]
    return max(sums)

data = [[1, 2, 3, 4],\
        [5, 6, 7, 8],\
        [9, 10, 11, 12],\
        [13, 14, 15, 16]]

print(sum_columns(data))