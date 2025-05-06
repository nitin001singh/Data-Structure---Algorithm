# Brute Force
# TC : O(N^2)
# Sc : O(1)

# class Solution:
#     def answer(self, nums, k):
#         n = len(nums)
#         count = 0
#         for x in range(n):
#             for y in range(x+1, n):
#                 if nums[x] - nums[y] == k:
#                     count += 1
        
#         return count
        
        
# response = Solution().answer([1,5,2,4,1],3)
# print(response)


# Optimal
# TC:O(N)
# SC:O(N)


class Solution:
    def answer(self, nums, k):
        count = 0
        hashmap = {}
        for num in nums:
            target = num - k
            count += hashmap.get(target, 0)
            hashmap[num] = hashmap.get(num, 0) + 1
        return count
        
        
response = Solution().answer([1,5,2,4,3],2)
print(response)
