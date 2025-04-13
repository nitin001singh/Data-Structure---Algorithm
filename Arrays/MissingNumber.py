# Brute force 

# TC : O(N2)
# SC : O(1)

# class Solution:
#     def missingNumber(self, nums):
#         if not nums :
#             return -1
#         n = len(nums)      
#         for index in range(n+1):
#             if index not in nums:
#                 return index
            
   
    
# result = Solution().missingNumber([9,6,4,2,3,5,7,0,1])  
# print(result)



# Optimal 

# TC : O(N)
# SC : O(1)

# class Solution:
#     def missingNumber(self, nums):
#         if not nums :
#             return -1
#         length= len(nums)
#         naturalSum =  length * ( length + 1 ) // 2
#         currentSum = sum(nums)

#         return naturalSum - currentSum

# result = Solution().missingNumber([3,0,1])
# print(result) 


# Using XOR
# TC : O(N)
# SC : O(1)

class Solution:
    def missingNumber(self, nums):
        nlenXor = 0
        for value in range(len(nums)+1):
            nlenXor ^= value
            
        xor = self.getXor(nums, nlenXor)
        
        return  xor
        
        
    def getXor(self, nums, nlenXor):
        for _, value in enumerate(nums):
            nlenXor ^= value
        return nlenXor

    
    
result =  Solution().missingNumber([3, 4 ,-1, 1])
print(result)