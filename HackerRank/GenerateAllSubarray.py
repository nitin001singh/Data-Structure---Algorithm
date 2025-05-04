# BruteForce 

# TC : O(N^3)
# SC : O(1)

def subArray(arr):
    n = len(arr)
    for x in range(n):
        for y in range(x,n):
            for k in range(x,y+1):
                print(arr[k], end=" ")
            print()


subArray([1, 2, 3, 4])