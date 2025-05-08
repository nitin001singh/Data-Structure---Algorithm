# Given an array of all integers>=0 -> find the largest subarray length whose sum is <= k



# Brute Force 
# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums, k):
#         n = len(nums)
#         maxLength = 0
#         for i in range(n):
#             summ = 0
#             length = 0
#             for j in range(i, n):
#                 summ += nums[j]
#                 if summ <= k:
#                     length = j - i + 1
            
#             maxLength = max(length, maxLength)
                                 
#         return maxLength
        
# result = Solution().answer([1,2,2,8,4,3], 12)
# print(result)



# Optimal 

# TC : O(2*N)  => O(N)
# Sc : O(1)



class Solution:
    def answer(self, nums, k):
        n = len(nums)
        maxLength = 0
        i = 0
        summ = 0
        for j in range(n):
            summ += nums[j]
            
            while summ > k:
                summ -= nums[i]
                i += 1
            
            length = j - i + 1
            maxLength = max(maxLength, length)
                
                                 
        return maxLength
        
result = Solution().answer([1,2,2,8,4,3], 12)
print(result)