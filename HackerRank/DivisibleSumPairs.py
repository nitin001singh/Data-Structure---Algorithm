def subArray(arr, k):
    n = len(arr)
    count = 0
    for x in range(n):
        for y in range(x+1, n):
            if (arr[x] + arr[y]) % k == 0:
                count += 1
    return count


res = subArray([1,3,2,6,1,2], 3)
print(res)