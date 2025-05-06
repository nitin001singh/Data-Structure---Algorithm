# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, arr1):
        hashmap = {}
        n = len(arr1)
        for value in arr1:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1


        maxFreq = float("-inf")
        for index,value in hashmap.items():
            if value > maxFreq:
                maxFreq = value
                
        return n - maxFreq
        

res = Solution().answer([9,3,1,5,2,1])
print(res)