

# Single Rotate
# TC : O(N)
# SC : O(N)
# class Solution:
#     def answer(self, nums, key):
#         n = len(nums)
#         temp = [0] * n
#         for index in range(1, len(nums)):
#             temp[index - 1] = nums[index]

#         temp[n-1] = nums[0]
        
#         return temp
        
        
# result = Solution().answer( [1,2,3,4,5,6,7] , 1 )  
# print(result)   


# Single Rotate
# TC : O(N)
# SC : O(1)
# class Solution:
#     def answer(self, nums, key):
#         n = len(nums)
#         # temp = [0] * n
#         temp = nums[0]
#         for index in range(1, len(nums)):
#             nums[index - 1] = nums[index]

#         nums[n-1] = temp
        
#         return nums
        
        
# result = Solution().answer( [1,2,3,4,5,6,7] , 1 )  
# print(result)   



# Optimal

# TC : O(N)
# SC : O(1)


class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
        return nums
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
        return nums
        

result = Solution().rotate([1,2,3,4,5,6,7] , 4)
print(result)