class Solution :
    def answer(self , nums, key):
        start = 0
        end =  len(nums) - 1 
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] == key:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= key <= nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
                    
            else:
                if nums[mid] <= key <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                
        return -1
    
result = Solution().answer([4, 5, 6, 7, 0, 1, 2], 0)
print(result)