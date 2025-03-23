# Brute Force 
# TC : O(N)
# SC : O(N)

# class Solution:
#     def productExceptSelf(self, nums):
#         product = 1
#         zeroCount = 0
#         for outer in range(len(nums)):   
#             if nums[outer] != 0:
#                 product *= nums[outer]
#             else :
#                 zeroCount += 1
          
#         if zeroCount > 1:
#             return [ 0 for _ in nums]
        
#         resp = []
#         for index, value in enumerate(nums):
#             if value == 0:
#                 resp.append(product)
#             else:
#                 if zeroCount == 1:
#                     resp.append(0)
#                 else:
#                     resp.append(product // value)
                  
#         return resp
    
    
# s = Solution()
# result = s.productExceptSelf([-1,1,0,-3,3])
# print(result)


# Optimize Solution
# TC : O(N)
# SC : O(N)

class OptimizeSolution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n
        
        product = 1
        for index in range(n):
            output[index] = product
            product *= nums[index]
            
        product = 1
        for index in range(n-1 , -1 , -1):
            output[index] *= product
            product *= nums[index]        

        return output
    
s = OptimizeSolution()
result = s.productExceptSelf([-1,1,0,-3,3])
print(result)
