# Brute Force 
# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums, k):
#         n = len(nums)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 diff = abs(nums[i] - nums[j])
#                 if diff == k:
#                     count += 1
                    
#         return count
        
        
        
# result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 2)
# print(result)



# Optimize 
# TC : O(N)
# SC : O(N)



class Solution:
    def answer(self, nums, k):
        count = 0
        freq = {}
    
        for j in range(len(nums)):
            
            if nums[j] - k in freq:
                count += freq[nums[j] - k]
                
            if k != 0 and nums[j] + k in freq: 
                count += freq[nums[j] + k]
    
            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1
    
        return count
        
                
result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 2)
print(result)