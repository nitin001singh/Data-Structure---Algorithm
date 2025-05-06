class Solution :
    def answer(self, arr):
        hashmap = {}
        for value in arr:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1



        maxElem = 0
        maxFreq = float("-inf")
        minElem = 0
        minFreq = float("inf")
        
        
        for number, freq in hashmap.items():
            if freq >= maxFreq:
                maxFreq = freq
                maxElem = number
            else:
                minFreq = freq
                minElem = number


        return  "Max Element is {} with frequency {} and Min Element is {} with frequency {}".format(maxElem, maxFreq, minElem, minFreq)
         

res = Solution().answer([9,3,1,5,2,1,9,9])
print(res)