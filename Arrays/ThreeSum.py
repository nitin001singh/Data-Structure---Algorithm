# Brute force 
# TC : O(n^3)
# SC : O(k) k is the unique triplets

# class Solution:
#     def answer(self, nums):
#         n = len(nums)
#         if n < 3:
#             return 0
#         opt = set()
#         for i in range(n):
#             for j in range(i+1, n) :
#                 for k in range(j+1, n):
#                     if nums[i] + nums[j] + nums[k] == 0 :
#                         result = tuple(sorted([nums[i], nums[j], nums[k]]))
#                         opt.add(result)

#         return opt
        
# result = Solution().answer(  [-1,0,1,2,-1,-4] )  
# print(result)   

# Optimal 

# TC : O(n^2)
# SC : O(k)

class Solution:
    def threeSum(self, nums):
        nums.sort() 
        hashset = set()

        tar = 0
        for i in range(len(nums)):
            ntar = tar - nums[i]
            
            left = i +1
            right = len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] < ntar:
                    left += 1
                elif nums[left] + nums[right] > ntar:
                    right -= 1
                else:
                    hashset.add((nums[i] , nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
        return [ list(triplet) for triplet in hashset ]
 
        
result = Solution().threeSum(  [-1,0,1,2,-1,-4] )  
print(result)   