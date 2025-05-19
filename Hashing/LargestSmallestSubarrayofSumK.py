# Brute Force 

# TC : O(N^2)
# SC : O(N)

# class Solution:
#     def answer(self , nums, k ):
        
#         minLength = float("inf")
#         maxLength = float("-inf")
#         maxResult = [0,0]
#         minResult = [0,0]
        
#         n = len(nums)
#         for i in range(n):
#             summ = 0
#             for j in range(i, n ):
#                 summ += nums[j]
#                 if summ == k :
#                     if ( j - i + 1) > maxLength:
#                         maxLength = (j-i + 1)
#                         maxResult[0] = i
#                         maxResult[1] = j
#                     else:
#                         minLength = j - i + 1
#                         minResult[0] = i
#                         minResult[1] = j
                    
        
#         return maxLength, maxResult, minLength, minResult
        
# result = Solution().answer([1, 2, 3, 4, 5, -1, 6], 9)
# print(result)



class Solution:
    def answer(self , nums, k ):
        
        summ = 0
        length = 0
        n = len(nums)
        hashmap = {}
        hashmap = {0: -1}
        for i in range(n):
            summ += nums[i]
            if summ == k:
                length = max(length, i+1)
            
            if summ not in hashmap:
                hashmap[summ] = i
                
            if summ - k in hashmap:
                length = max(length, i-hashmap[summ-k])
                
            
        return length
    
    
    def smallest(self , nums, k ):
        
        summ = 0
        length = float("inf")
        n = len(nums)
        hashmap = {}
        hashmap = {0: -1}
        for i in range(n):
            summ += nums[i]
            if summ == k:
                length = min(length, i+1)
            
            if summ not in hashmap:
                hashmap[summ] = i
                
            if summ - k in hashmap:
                length = min(length, i-hashmap[summ-k])
                
            
        return length
            
        
result = Solution().answer([1, 2, 3, 4, 5, -1, 6], 9)
result1 = Solution().smallest([1, 2, 3, 4, 5, -1, 6], 9)
print(result,', ' ,result1)