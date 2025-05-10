# Single Element in a Sorted Array

# TC : O(logN)
# SC : O(1)


class Solution:
    def answer(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


                            

result = Solution().answer( [1,1,2,3,3,4,4,8,8])
print(result)