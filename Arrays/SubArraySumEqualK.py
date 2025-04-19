# Brute Force 

# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self , nums, k):
#         maxCount = 0
#         for i in range(len(nums)):
#             summ = 0
#             for j in range(i, len(nums)):
#                 summ += nums[j]
#                 if summ == k:
#                     maxCount += 1
                    
#         return maxCount
                
# result = Solution().answer([1,2,3], 3)
# print(result)


# Optimal 

# TC : O(N)
# SC : O(1)

class Solution:
    def answer(self , nums, k):
        count = 0
        prefixSum = 0
        hashmap = {0: 1}

        for num in nums:
            prefixSum += num
            if (prefixSum - k) in hashmap:
                count += hashmap[prefixSum - k]
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1

        return hashmap, count
                
result = Solution().answer([1,2,3,2,8,6], 6)
print(result)