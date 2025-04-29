# Tc : O(N) & O(N^2) in worst case
# SC : O(1) 


class Insertion:
    def sorting(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
        
    
result = Insertion().sorting( [64, 25, 12, 22, 11] )
print(result)