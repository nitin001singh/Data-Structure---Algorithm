# TC : O(n^3)
# SC : O(n^3)

class Solution:
    def fourSum(self, nums, target):
        nums.sort() 
        return self.getFourSum(nums, target)
    
    def getFourSum(self, nums, target):
        hashset = set()
        for m in range(len(nums)-3):
            ntar = target - nums[m]
            for i in range(m + 1, len(nums) - 2):               
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i]  + nums[left] + nums[right] < ntar:
                        left += 1
                    elif nums[i]  + nums[left] + nums[right] > ntar:
                        right -= 1
                    else:
                        hashset.add((nums[m], nums[i] , nums[left], nums[right]))
                        left += 1
                        right -= 1
                    
        return [ list(triplet) for triplet in hashset ]


 
        
result = Solution().fourSum( [1,0,-1,0,-2,2] , 0)  
print(result)   