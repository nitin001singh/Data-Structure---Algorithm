# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, arr, k):
        hashset = set()
        for value in arr:
            temp = k - value
            if temp in hashset:
                return True
            
            hashset.add(value)
        
        return False
        

res = Solution().answer([1,2,3,1],3)
print(res)