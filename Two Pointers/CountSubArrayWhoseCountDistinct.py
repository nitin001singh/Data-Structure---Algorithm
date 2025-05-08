# Tc : O(N^2)
# Tc : O(1)

class Solution:
    def answer(self, nums, k):
        count = 0
        for j in range(len(nums)):
            hashmap = {}
            for z in range(j, len(nums)):
                hashmap[nums[z]] = hashmap.get(nums[z], 0) + 1
                print(hashmap)
                n = len(hashmap)
                if n <= k:
                    count += 1
                    
        return count
            

result = Solution().answer([1 ,2 ,3 ], 2)
print(result)
