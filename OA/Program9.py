
# TC : O(N * M)  n = number of test cases  m = size of each array
# SC : O(N)

class Solution:
    def answer(self):
        n = int(input("Enter number of test cases: "))
        
        opt = []
        for i in range(n):
            size = int(input("Enter the size of an array : "))
            a = [0]
            for x in range(1,size+1):
                a.append(
                    int(input("Enter value of array: "))
                )
                
            hashmap = {}
            count = 0
            for i in range(1, len(a)):
                rhs = a[a[a[i]]]
                g = hashmap.get(rhs, 0)
                count += g

                    
                lhs = a[a[a[i]]]
                hashmap[lhs] = hashmap.get(lhs, 0) + 1
                
            opt.append(count)
        return opt
        
     
        
result = Solution().answer()
for x in result:
    print(x , end="\n")
