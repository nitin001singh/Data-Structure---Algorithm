# Optimal 

# TC: O(N)
# SC: O(1)

class SortArray:
    def sorting(self , nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        
        left = 0
        mid = 0
        right = len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[mid] , nums[left] = nums[left], nums[mid]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid] , nums[right] = nums[right], nums[mid]
                right -= 1
                    
        return nums

res = SortArray().sorting([0,1,2,1,2,0])
print(res)


