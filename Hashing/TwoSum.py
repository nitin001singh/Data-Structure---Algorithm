# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, nums, target):
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [index, hashmap[diff]]
                
            hashmap[value] = index
                

res = Solution().answer([2,7,11,15],9)
print(res)