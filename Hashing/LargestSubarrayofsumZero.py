# SC : O(N)
# SC : O(N)

class Solution:
    def answer(self , nums, k ):
        summ = 0
        length = 0
        n = len(nums)
        hashmap = {}
        hashmap[0] = 1
        for i in range(n):
            summ += nums[i]
            if summ == k:
                length = max(length, i+1)
            
            if summ not in hashmap:
                hashmap[summ] = i
                
            if summ - k in hashmap:
                length = max(length, i-hashmap[summ-k])
                
            
        return length
            
        
result = Solution().answer( [15, -2, 2, -8, 1, 7, 10, 23], 0)
print(result)