def InsertionSort(arr):
    # n = len(arr)
    # for i in range(1, n):
    #     for j in range(i,0,-1):
    #         if arr[j] < arr[j-1]:
    #             arr[j] , arr[j-1] = arr[j-1] , arr[j]
    #         else:
    #             break
    # return arr
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(" ".join(list(map(str, arr))))
            j -= 1
        arr[j + 1] = key
    print(" ".join(list(map(str, arr))))
res = InsertionSort([2,4,6,8,3])
print(res)

