def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        return arr[n // 2]
    else:
        first = arr[(n // 2) - 1]
        second = arr[(n // 2)]
        return (first + second) / 2


res = findMedian([0 ,1 ,2 ,4 ,5 ,3])
print(res)


# 0 1 2 3 4 5