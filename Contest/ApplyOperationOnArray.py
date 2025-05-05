def getZeroLast(arr):
    starting = 0
    for x in range(len(arr)):
        if arr[x] != 0:
            arr[x], arr[starting] = arr[starting] , arr[x]
            starting += 1
    
    return arr
    

def applyOperation(arr):
    n = len(arr)
    for index in range(n-1):
        if arr[index] == arr[index + 1]:
            arr[index] *= 2
            arr[index + 1] = 0
        else:
            continue

   
    res = getZeroLast(arr)
    return res
    
res = applyOperation([1,2,2,1,1,0])
print(res)


# [1,4,0,2,0,0]