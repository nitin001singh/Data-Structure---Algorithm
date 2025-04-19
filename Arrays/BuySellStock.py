# Brute Force 

# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self , nums):
#         maxPro = 0
#         for i in range(len(nums)):
#             for j in range(i+1 , len(nums)):
#                 if nums[j] > nums[i]:
#                     maxPro = max(maxPro, nums[j] - nums[i])
#         return maxPro
    
    
# result = Solution().answer([7,1,5,3,6,4])
# print(result)


# Optimal 
# Tc: O(N)
# SC : O(1)

class Solution:
    def answer(self , nums):
        mini = nums[0]
        maxPro = 0
        for index in range(len(nums)):
            if nums[index] > mini:
                maxPro = max(maxPro , nums[index] - mini)
            else:
                mini = nums[index]
            
            
        return maxPro
    
    
result = Solution().answer([1,2,4,5,9,7,2,3])
print(result)
