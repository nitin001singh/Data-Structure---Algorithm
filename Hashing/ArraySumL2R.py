# Brute Force 
# TC : O(N)
# SC : O(N)

# class Solution:
#     def answer(self, nums, l, r):
#         return sum(nums[l: r+1])    # Create new list 
        
        
        
# result = Solution().answer([1, 7, 5, 9, 2, 12, 3],2,3)
# print(result)


# Optimal 
# TC : O(N+Q)  => O(N)
# SC : O(N)


class Solution:
    def answer(self, nums, l, r):
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for index in range(1, n):
            prefixSum[index] =  prefixSum[index - 1] + nums[index]
            
        sumFroml2R = prefixSum[r] - prefixSum[l-1] 
    
        return sumFroml2R 
        
        
result = Solution().answer([1, 7, 5, 9, 2, 12, 3] , 2 , 3)
print(result)