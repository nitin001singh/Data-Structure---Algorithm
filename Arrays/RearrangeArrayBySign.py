# Brute Force 
# TC : O(N)
# SC : O(N)

# class Solution:
#     def answer(self , nums):
#         positiveNum = []
#         negativeNum = []
        
#         for value in nums:
#             if value > 0 :
#                 positiveNum.append(value)
#             else:
#                 negativeNum.append(value)
        
        
#         resp = []
#         for item in zip(positiveNum, negativeNum):
#             fval, sval = item
#             resp.append(fval)
#             resp.append(sval)
            
#         return resp
    
    
# result = Solution().answer([-1,1])
# print(result)



# Optimal 
# TC : O(N)
# SC : O(N)


# class Solution:
#     def answer(self , nums):
#         n = len(nums)
#         ans = [0] * n
#         posIndex = 0
#         negativeIndex = 1
#         for value in nums:
#             if value < 0:
#                 ans[negativeIndex] = value
#                 negativeIndex += 2
#             else:
#                 ans[posIndex] = value
#                 posIndex += 2
                
#         return ans
                

    
# result = Solution().answer([3,1,-2,-5,2,-4])
# print(result)


# if unequal number of elements in array then

# Brute Force 

# TC : O(N)
# SC : O(N)

# class Solution:
#     def answer(self , nums):
#         positiveNum = []
#         negativeNum = []
        
#         for value in nums:
#             if value > 0 :
#                 positiveNum.append(value)
#             else:
#                 negativeNum.append(value)
        
#         resp = []
#         i, j = 0, 0
        
#         while i < len(positiveNum) or j < len(negativeNum):
#             if i < len(positiveNum):
#                 resp.append(positiveNum[i])
#                 i += 1
#             if j < len(negativeNum):
#                 resp.append(negativeNum[j])
#                 j += 1
                
#         return resp
# result = Solution().answer([3,1,-2,-5,2,-4,-7])
# print(result)



