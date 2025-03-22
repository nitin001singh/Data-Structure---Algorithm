#Brute Force Approach
# TC: O(n²)
# SC: O(1)

# class Solution:
#     def twoSum(self, nums, target):
#         for outer in range(len(nums) - 1):
#             for inner in range(1, len(nums)):
#                 if nums[outer] + nums[inner] == target:
#                     return [outer , inner]
            

# s1 = Solution()
# result = s1.twoSum([2,7,11,15], 22)
# print(result)



# Optimize approach  
# TC: O(n)
# SC: O(n)

class OptimizeSolution:
    def twoSum(self, nums , target):
        hashmap = {}
        for outer in range(len(nums)):
            if (target - nums[outer]) in hashmap:
                return [outer, hashmap[(target - nums[outer])]]
            hashmap[nums[outer]] = outer
    
s1 = OptimizeSolution()
result = s1.twoSum([2,7,11,15],18)
print(result)