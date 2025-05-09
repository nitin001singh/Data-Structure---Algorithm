# Find First and Last Position of Element in Sorted Array

# TC : O(NlogN)
# SC : O(1)
class Solution:
    def answer(self, nums, target):
        nums.sort()
        opt = [-1,-1]
        for x in range(len(nums)):
            if nums[x] == target:
                opt[0] = x
                break
            
        for y in range(len(nums)-1, -1 ,-1):
            if nums[y] == target:
                opt[1] = y
                break
            
        return opt       
        
result = Solution().answer([1,2,3,4,5,4,6,8,1,4], 4)
print(result)