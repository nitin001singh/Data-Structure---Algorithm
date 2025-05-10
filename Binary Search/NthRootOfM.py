# Find nth root of m
# Brute Force
# Tc : O(N)
# SC : O(1)

# class Solution:
#     def answer(self, m,n):
#         i = 1
#         while i**n <= m:
#             if m == i**n:
#                 return i
#             i += 1
            
#         return -1           
                
# result = Solution().answer(9,2)
# print(result)



class Solution:
        
    def answer(self, m,n):
        l = 1 
        r = m
        
        while l <= r:
            mid = (l+r) // 2
            
            if mid**n == m:
                return mid
            
            if mid ** n > m:
                r = mid - 1
                
            else:
                l = mid + 1
                
        return -1      
                
result = Solution().answer(9,2)
print(result)