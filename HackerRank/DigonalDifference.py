def diagonalDifference(arr):
    leftDigonal = 0
    rightDigonal = 0
    
    m = len(arr)
    n = len(arr[0])
    
    for row in range(m):
        for col in range(n):
            if row == col:
                leftDigonal += arr[row][col]
               
            if col == n - row -1:
                rightDigonal += arr[row][col] 
                   
    return abs(leftDigonal - rightDigonal)
                
res = diagonalDifference([[1,2,3],[4,5,6],[9,8,9]])
print(res)
