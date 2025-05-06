# Brute Force 
# Tc : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums,k):
#         n = len(nums)
#         count = 1
#         for i in range(n):
#             currentSum = 0
#             for j in range(i, n):
#                 currentSum += nums[j]
#                 if currentSum == k:
#                     count += 1
                    
                
#         return count
            
    
# result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 9)
# print(result)



class Solution:
    def answer(self, nums, k):
        count = 0
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        for i in range(n):
            for j in range(i, n):
                subarray_sum = prefix_sum[j] - (prefix_sum[i - 1] if i > 0 else 0)
                # print(subarray_sum)
                if subarray_sum == k:
                    count += 1
        
        return count

result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 9)
print(result)



