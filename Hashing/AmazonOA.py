# "Given an array find two subarrays of maximum sum which are not intersecting    (AMAZON OA)"

class Solution:
    def answer(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        prefixSumm = self.getPrefixSum(nums)
        suffixSumm = self.getSuffixSum(nums)
        
        max_total = float('-inf')
        for i in range(n - 1):
            max_total = max(max_total, prefixSumm[i] + suffixSumm[i + 1])

        return prefixSumm, suffixSumm, max_total
        
    def getPrefixSum(self, nums):
        n = len(nums)
        pSum = [0] * n
        currentMax = nums[0]
        pSum[0] = currentMax
        
        for i in range(1, n):
            currentMax = max(nums[i], currentMax + nums[i])
            pSum[i] = max(pSum[i-1], currentMax)
        
        return pSum
            
    def getSuffixSum(self, nums):
        n = len(nums)
        sSum = [0] * n
        currentMax = nums[-1]
        sSum[-1] = currentMax

        for i in range(n - 2, -1, -1):
            currentMax = max(nums[i], currentMax + nums[i])
            sSum[i] = max(sSum[i+1], currentMax)
        
        return sSum
        
      
result = Solution().answer([1, 3, -1, 2, -1, 2, -1, 2])
print(result)
