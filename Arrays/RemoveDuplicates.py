# Brute force
# TC : O(n)
# SC : O(n)  

# it does not work in place so this solution is not correct as per our requiremnt

# class Solution:
#     def removeDuplicates(self, nums):
#         unique_arr = list(set(nums))
#         return unique_arr
    
    
# s = Solution()
# result = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# print(result)



# Optimize Approach 
# TC : O(n)
# SC : O(1)

class OptimizeSolution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        for _ in range(len(nums) - 1):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        
        return i+1
    
    
s = OptimizeSolution()
result = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)