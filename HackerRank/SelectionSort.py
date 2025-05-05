# Tc : O(N^2)
# SC : O(1) 


# Selection Sort
def SelectionSort(arr):
    n = len(arr)
    for index in range(n):
        minIndex = index
        for innerIndex in range(index + 1, n):
            if arr[innerIndex] < arr[minIndex]:
                minIndex = innerIndex
                
        arr[index], arr[minIndex] = arr[minIndex], arr[index]
        
    return arr

res = SelectionSort([2,4,6,8,3])
print(res)

