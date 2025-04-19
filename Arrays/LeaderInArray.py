# Brute Force 

# Tc : O(N)
# Tc : O(N)

# import sys
# class Solution:
#     def answer(self , nums):
#         n = len(nums)
#         resp = []
#         for index in range(n-1):
#             greater = -sys.maxsize
#             for j in range(index+1, n):
#                 if nums[j] > greater:
#                     greater = nums[j]
            
#             if nums[index] > greater:
#                 resp.append(nums[index])
             
             
#         resp.append(nums[n-1])
                    
#         return resp
            
    
# result = Solution().answer(  [10, 22, 12, 3, 0, 6] )
# print(result)


# Optimal 
# TC : O(N)
# TC : O(N)

# import sys
# class Solution:
#     def answer(self , nums):
#         n = len(nums)
#         resp = []
#         greater = -sys.maxsize
#         for index in range(n-1, -1, -1):
#             if nums[index] > greater:
#                 resp.append(nums[index])
#                 greater = nums[index]
            
                    
#         return resp
            
    
# result = Solution().answer(  [4, 7, 1, 0] )
# print(result)