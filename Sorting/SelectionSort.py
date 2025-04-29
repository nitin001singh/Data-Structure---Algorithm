# Tc : O(N^2)
# SC : O(1) 


class Selection:
    def sorting(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i 
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
        
    
result = Selection().sorting( [64, 25, 12, 22, 11] )
print(result)