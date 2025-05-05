def runningTime(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                count += 1
                arr[j] , arr[j-1] = arr[j-1] , arr[j]
            else:
                break
    return count


res = runningTime([2, 1, 3, 1, 2])
print(res)