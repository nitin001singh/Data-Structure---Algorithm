# Range Updater

# Tc: O(N)
# SC : O(1)


class Solution:
    def answer(self, nums, rangearr):
        for rlist in rangearr:
            l, r  = rlist
            nums[l] += 1
            nums[r+1] += -1
            

        for x in range(1, len(nums)):
            nums[x] = nums[x -1] + nums[x]
        
        return nums
            
  
        
result = Solution().answer([0,0,0,0,0,0,0,0,0,0],[[1,3],[5,8]])
print(result)