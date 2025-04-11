# Brute Force 

# TC : O(N)
# SC : O(N)

# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         return nums[n-k:] + nums[:n-k]
        

# result = Solution().rotate([1,2,3,4,5,6,7] , 2)
# print(result)


# Optimal

# TC : O(N)
# SC : O(1)



class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
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
        

result = Solution().rotate([1,2,3,4,5,6,7] , 3)
print(result)