# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, arr1 , arr2):
        hashmap = {}
        for value in arr1:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1


        for value in arr2:
            if value not in hashmap or hashmap[value] == 0:
                return False
            
            hashmap[value] -= 1
        return True
         

res = Solution().answer([9,3,1,5,2,1],[9,1,1,1])
print(res)