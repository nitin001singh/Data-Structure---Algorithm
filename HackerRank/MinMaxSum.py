def miniMaxSum(arr):
    # Write your code here
    output = []
    for x in range(len(arr)):
        totalCount = 0
        for y in range(len(arr)):
            if x != y:
                totalCount += arr[y]
        output.append(totalCount)

    print( min(output) , end=" ")
    print( max(output) , end=" ")
    
res = miniMaxSum([5,5,5,5,5])
# print(res)