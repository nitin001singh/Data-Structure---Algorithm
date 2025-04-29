# Tc : O(N) & O(N^2) in worst case
# SC : O(1) 


class Bubble:
    def sorting(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
        
    
result = Bubble().sorting( [64, 25, 12, 22, 11] )
print(result)