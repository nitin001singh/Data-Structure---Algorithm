# Brute Force
# TC : O(N^5)
# SC : O(1)

class Solution:
    def answer(self, a,b,c,d,e):
        count = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    for l in range(len(d)):
                        for m in range(len(e)):
                            
                            if (a[i] + b[j] + c[k] + d[l] + e[m]) == 0:
                                count += 1
        return count

        
result = Solution().answer([2 ,5],  [3 ,8], [-5 ,8],[5 ,10], [-10 , 100] )
print(result)



# TC : O(N^4)
# SC : O(N)


class Solution:
    def answer(self, a,b,c,d,e):
        
        hashmap = {}
        
        for x in e:
            hashmap[x] = hashmap.get(x, 0) + 1
        
        count = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    for l in range(len(d)):
                        y = -(a[i] + b[j] + c[k] + d[l])
                        if y in hashmap:
                            count += hashmap[y]
        return count

        
result = Solution().answer([2 ,5],  [3 ,8], [-5 ,8],[5 ,10], [-10 , 100] )
print(result)




# TC : O(N^3  + N ^2)
# SC : O(N ^ 2 )


class Solution:
    def answer(self, a,b,c,d,e):
        
        hashmap = {}
        
        for x in d:
            for z in e: 
                # print(x,z)
                summ = x + z
                hashmap[summ] = hashmap.get(summ, 0) + 1
            
        # print(hashmap)
        
        count = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    y = -(a[i] + b[j] + c[k])
                    if y in hashmap:
                        count += hashmap[y]
        return count

        
result = Solution().answer([2 ,5],  [3 ,8], [-5 ,8],[5 ,10], [-10 , 100] )
print(result)