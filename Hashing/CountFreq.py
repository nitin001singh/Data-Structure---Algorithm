# TC : O(N+Q)
# SC : O(N)

class Solution :
    def answer(self):
        n = int(input("No. of elements : "))
        hashMap = {}
        for elemCount in range(n):
            value = int(input("Enter element {}".format(elemCount+1) + " : "))
            if value in hashMap:
                hashMap[value] += 1
            else:
                hashMap[value] = 1                
            
            
        q = int(input("Enter number of Queries : "))
        
        for elemCount in range(q):
            qVal = int(input("Enter query {}".format(elemCount+1) + " : "))
            print(qVal , "is", hashMap.get(qVal, 0), "times in list")
        
        
res = Solution().answer()
print(res)