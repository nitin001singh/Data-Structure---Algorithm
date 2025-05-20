# We are given an array of size N ; we are told to pick up any 2 numbers from the array such that their digit sum is equal ; if their digit sum is equal ; calculate their sum ; question is saying to find the maximum possible sum 


# TC : O(N^2)
# SC: O(1)

class Solution:
    def answer(self, nums):
        n = len(nums)
        
        ans = 0
        for i in range(1,n):
            j = i - 1
            while j >= 0:
                if self.digiSum(nums[i]) == self.digiSum(nums[j]):
                    summ = nums[i] + nums[j]
                    ans = max( ans, summ)
                
                j -= 1
                
        return ans            
            
            
    def digiSum(self, num):
        summ = 0
        while num > 0:
            summ += num % 10
            num //= 10
            
        return summ
        

result = Solution().answer([51 ,71 ,17 ,42] )
print(result)