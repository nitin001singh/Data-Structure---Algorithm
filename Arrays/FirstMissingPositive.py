class Solution:
    def answer(self, arr):
        n = len(arr)
        # if 0 or less than 0 then set value to n + 1
        for index in range(n):
            if arr[index] <= 0:
                arr[index] = n + 1
        
        # print('Arr1 ',arr)
        
        for index in range(n):
            value = abs(arr[index])
            if 0 < value <= n:
                arr[value-1] = -1 * abs(arr[value - 1])
                
        # print('Arr2 ',arr)
    
        for index in range(n):
            if arr[index] > 0:
                return index + 1
    
        return n + 1
    
            
result = Solution().answer([3 ,4 ,1, 2]) 
print(result)   


