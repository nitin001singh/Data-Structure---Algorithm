# Tc : O(n log n) & O(n^2) in worst case
# SC : O(nlogn) 


class Insertion:
    def sorting(self, arr):
        if len(arr) <= 1:
            return arr 
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot] 
        right = [x for x in arr[:-1] if x > pivot]
        return self.sorting(left) + [pivot] + self.sorting(right)
            
    
result = Insertion().sorting( [64, 25, 12, 22, 11] )
print(result)