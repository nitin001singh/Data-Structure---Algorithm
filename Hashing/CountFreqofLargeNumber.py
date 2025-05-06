# TC : O(N)
# SC : O(N)


class Solution :
    def answer(self, nums):
        hashmap = {}
        for value in nums:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1
                
        return hashmap
        
        
res = Solution().answer([1,2,3,4,5,4,5,1,1])
print(res)