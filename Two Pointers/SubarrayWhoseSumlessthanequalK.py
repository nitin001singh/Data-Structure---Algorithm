class Solution:
    def answer(self, nums, k):
        
        i = 0
        summ = 0
        count = 0
        for j in range(len(nums)):
            summ += nums[j]
            
            if summ > k:
                while summ > k:
                    summ -= nums[i]
                    i += 1
            count += j - i + 1
        return count
        
        
    
result = Solution().answer([1,2,2,8,4,3], 4)
print(result)