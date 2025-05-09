# Find First and Last Position of Element in Sorted Array

# TC : O(NlogN)
# SC : O(1)
# class Solution:
#     def answer(self, nums, target):
#         nums.sort()
#         opt = [-1,-1]
#         for x in range(len(nums)):
#             if nums[x] == target:
#                 opt[0] = x
#                 break
            
#         for y in range(len(nums)-1, -1 ,-1):
#             if nums[y] == target:
#                 opt[1] = y
#                 break
            
#         return opt       
        
# result = Solution().answer([1,2,3,4,5,4,6,8,1,4], 4)
# print(result)





# TC : O(NlogN)
# SC : O(1)
class Solution:
    def answer(self, nums, target):
        nums.sort()
        opt = [-1,-1]
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                opt[0] = mid
                r = mid -1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
            
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                opt[1] = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1       

        return opt       
        
result = Solution().answer([5,7,7,8,8,10], 8)
print(result)