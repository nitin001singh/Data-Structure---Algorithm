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



class Solution:
    def answer(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index] != nums[index-1]: continue
            left = index + 1
            right = n-1
            
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                            
        return result     
        
result = Solution().answer(  [-1,0,1,2,-1,-4] )  
print(result)   