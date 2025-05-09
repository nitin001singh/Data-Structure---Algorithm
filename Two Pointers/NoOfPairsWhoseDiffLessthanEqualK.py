# Number of pairs whose diff <=K (


# Tc : O(N^2) + O(NlogN)   == >   O(N^2)
# Tc : O(1)

# class Solution:
#     def answer(self, nums, k):
#         count = 0
#         nums.sort()
#         n = len(nums)
#         for i in range(n):
#             for j in range(i, n):
#                 diff = nums[j] - nums[i]
#                 if diff <= k:
#                     count += 1
                    
#         return count - n
            

# result = Solution().answer([1 ,2 ,3 , 4, 5], 2)
# print(result)




class Solution:
    def answer(self, nums, k):
        count = 0
        n = len(nums)
        nums.sort()
        left = 0
        right = 0
        for right in range(n):
            diff = nums[right] - nums[left]
            while diff > k:
                left += 1
                diff = nums[right] - nums[left]
            count += right - left + 1
            right += 1
            
        return count - n
                
        

result = Solution().answer([1 ,2 ,3 , 4, 5], 2)
print(result)