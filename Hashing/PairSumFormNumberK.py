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


# Count Number of Pairs 

class Solution :
    def answer(self, arr, k):
        hashset = set()
        count = 0
        for value in arr:
            temp = k - value
            if temp in hashset:
                count += 1
            
            hashset.add(value)
        
        return count
        

res = Solution().answer([1, 2, 3, 4, 5],6)
print(res)