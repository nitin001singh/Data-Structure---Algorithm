# Tc : O(n log n) in worst case
# SC : O(n) 


class Merge:
    def sorting(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid] 
            right = arr[mid:]

            self.sorting(left)  
            self.sorting(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

        
    
result = Merge().sorting( [38, 27, 43, 3, 9, 82, 10] )
print(result)