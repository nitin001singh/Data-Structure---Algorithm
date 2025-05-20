# We are given an array of size N ; we are told to pick up any 2 numbers from the array such that their digit sum is equal ; if their digit sum is equal ; calculate their sum ; question is saying to find the maximum possible sum 

# BruteForce
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
            
             
    def digiSum(self, num):    # TC: O(log10(num))
        summ = 0
        while num > 0:
            summ += num % 10
            num //= 10
            
        return summ
        

result = Solution().answer([51 ,71 ,17 ,42] )
print(result)




# Optimal
# TC : O(N)
# SC : O(1)

class Solution:
    def answer(self, nums):
        hashmap = {}
        maxi = 0
        for val in nums:
            digi_sum = self.digiSumMap(val)
            if digi_sum in hashmap:
                summ = hashmap[digi_sum] + val
                maxi = max(maxi, summ)
                    
            else:
                hashmap[digi_sum] = val
                
        return  maxi           

             
    def digiSumMap(self, num):    # TC: O(log10(num))
        summ = 0
        while num > 0:
            summ += num % 10
            num //= 10
            
        return summ
        

result = Solution().answer([51 ,71 ,17 ,42] )
print(result)