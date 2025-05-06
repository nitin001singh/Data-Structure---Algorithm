# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, arr1 , arr2):
        hashset = set()
        for value in arr1:
            hashset.add(value)
            
        for value in arr2:
            if value not in hashset:
                return False
            
        return True
         

res = Solution().answer([2,4,7,1,5],[5,4,2])
print(res)