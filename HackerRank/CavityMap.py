def cavityMap(matrix):
    m = len(matrix)
    n = len(matrix[0])
    opt = [[0 for _ in range(n)] for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if row == 0 or row == m - 1 or col == 0 or col == n-1:
                opt[row][col] = matrix[row][col]
            elif (matrix[row][col] >  matrix[row][col-1])  and (matrix[row][col] >  matrix[row][col+1]) and (matrix[row][col] >  matrix[row-1][col]) and (matrix[row][col] > matrix[row+1][col]):
                opt[row][col] = 'X'
            else:
                opt[row][col] = matrix[row][col]

    res = []
    for x in opt:
        res.append("".join(x))
    return res
        
    
res = cavityMap(['1112', '1912', '1892', '1234'])
print(res)

# 1 1 1 2
# 1 9 1 2
# 1 8 9 2
# 1 2 3 4 