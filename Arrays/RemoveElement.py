# Brute Force 

# TC : O(N)
# SC : O(N)


# class Solution:
#     def removeElement(self, nums, key):
#         res = []
#         for value in nums:
#             if value != key:
#                 res.append(value)
                
#         return len(res)
    
    
# result = Solution().removeElement([0,1,2,2,3,0,4,2], 2)
# print(result)   


# Optimize Solution
# TC : O(N)
# SC : O(1)

class OptimizeSolution:
    def removeElement(self, nums, key):
        i = 0
        for index in range(len(nums)):
            if nums[index] != key:
                nums[i] = nums[index]
                i += 1
        return i
    
result = OptimizeSolution().removeElement([3,2,2,3], 3)
print(result)   