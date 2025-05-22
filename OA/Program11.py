# Tc : O(N)
# SC : O(N)

class Solution:
    def answer(self, nums, k):
        n = len(nums)
        sSum = [0] * (n + 1)
        sSum[n-1] = nums[n-1]
       
        for x in range(n-2, -1, -1):    # Suffix sum
            sSum[x] = nums[x] + sSum[x+1] 


        pSum = 0
        ans = 0
        summ = 0
        
        for y in range(k):
            pSum = nums[y] + pSum
            summ = sSum[ n - k + (y+1) ]     # this formula is important    n - k + (y+1)  evaluate it 
            
            ans = max(ans, pSum + summ)
            
            
        return ans

        
result = Solution().answer([5, -2, 3, 1, 2], 3)
print(result)