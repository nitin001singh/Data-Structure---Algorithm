# TC : O(N)
# SC : O(N)

class Solution:
    def answer(self, nums):
        hashmap = {}
        maxi = 0
        for index in range(len(nums)):
            if nums[index] in hashmap:
                maxi = max(maxi, (index - hashmap[nums[index]]))
            else:
                hashmap[nums[index]] = index
            
        return  maxi
        
result = Solution().answer([1, 1, 2, 2, 2, 1])
print(result)