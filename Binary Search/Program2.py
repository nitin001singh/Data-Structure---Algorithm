# Given a sorted numsay of size “N”; find the index of the number in the array which is just greater than x and as close as possible to x.

# -> Upper Bound (x) = Returns index of the number which is just greater than x and as close as possible to x.




# TC : O(N)
# SC : O(1)


class Solution:
    def answer(self, nums, target):
        index = -1
        min_diff = float('inf')

        for i in range(len(nums)):
            if nums[i] > target and (nums[i] -target < min_diff):
                index = i
                min_diff = nums[i] - target

        return index
                            
result = Solution().answer([1, 3, 5, 7, 9, 11], 6)
print(result)




# TC : O(logN)
# SC : O(1)


class Solution:
    def answer(self, nums, x):
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > x:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
                            
                
    
    
result = Solution().answer( [1, 3, 5, 6, 6, 7, 7, 9], 6)
print(result)