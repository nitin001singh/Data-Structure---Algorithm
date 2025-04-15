# Brute force

# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self , nums, target):
        
#         length = 0
#         for i in range(len(nums)):
#             s = 0
#             for j in range(i, len(nums)):
#                 s += nums[j]
                
#                 if s == target:
#                     length = max(length, j-i +1 )
                    
#         return length
                    
    
    
# result = Solution().answer([-1, 1, 1], 1)
# print(result)


# Optimal 
# TC : O(N)
# SC : O(1)


class Solution:
    def answer(self , nums, k):
        
        summ = 0
        length = 0
        hashmap = {}
        for index, value in enumerate(nums):
            summ += value
            
            if summ == k :
                length = max(length, index + 1) 
                
            if summ not in hashmap:
                hashmap[summ] = index
                
            if summ - k in hashmap:
                length = max(length, hashmap[summ - k])
                    
        return length
    
result = Solution().answer([2,3,5], 5)
print(result)