# Longest Continuous Subarray With Absolute Diff Less Than or Equal to k


# Brute Force 
# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums, k):
#         max_len = 0
#         n = len(nums)
#         for i in range(n):
#             maxVal = nums[i]
#             minVal = nums[i]
#             for j in range(i, n):
#                 maxVal = max(maxVal, nums[j])
#                 minVal = min(minVal, nums[j])
                
#                 if maxVal - minVal <= k:
#                     max_len = max(max_len, j - i + 1)
#                 else:
#                     break
#         return max_len
                    

# result = Solution().answer([8,2,4,7], 4)
# print(result)




class Solution:
    def answer(self, nums, k):
        left = 0
        maxLength = 0

        for right in range(len(nums)):
            current_window = nums[left:right+1]
            while max(current_window) - min(current_window) > k:
                left += 1
                current_window = nums[left:right+1]
            
            maxLength = max(maxLength, right - left + 1)

        return maxLength
                    

result = Solution().answer([8,2,4,7], 4)
print(result)