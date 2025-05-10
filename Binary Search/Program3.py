#  Search in Rotated Sorted Array

# TC : O(logN)
# SC : O(1)


class Solution:
    def answer(self, nums, target):
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[0]:
                if target > nums[mid] or nums[0] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                
                if target < nums[mid]  or target > nums[n-1]:
                    right = mid - 1
                else:
                    left = mid + 1
                

        return -1
                            

result = Solution().answer( [10,12,15,20,25,30, 0,1,4,8], 0)
print(result)