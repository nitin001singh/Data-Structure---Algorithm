class Solution:
    def answer(self):
        
        n = int(input("Enter Male Numbers : "))
        arr1 = []
        arr2 = []
        for _ in range(n):
            arr1.append(int(input("Enter male array number : ")))
 
        for _ in range(n):
            arr2.append(int(input("Enter female array number : ")))
 

        # Process arrays
        p1m = []
        p2m = []
        for y in arr1:
            if y < 0:
                p2m.append(abs(y))
            else:
                p1m.append(y)
    
        p1f = []
        p2f = []
        for y in arr2:
            if y < 0:
                p2f.append(abs(y))
            else:
                p1f.append(y)
    
    
        # print(p1f ,  p2f)
        # Sort arrays
        p2m.sort()
        p1m.sort()
        p2f.sort()
        p1f.sort()
    
        # Count matches
        c = 0
        j = i = 0
        while i < len(p1f) and j < len(p2m):
            if p2m[j] > p1f[i]:
                c += 1
                j += 1
                i += 1
            else:
                j += 1
    
        j = i = 0
        while i < len(p1m) and j < len(p2f):
            if p2f[j] > p1m[i]:
                c += 1
                j += 1
                i += 1
            else:
                j += 1
    
        print(c)
        
        
        
result = Solution().answer()
print(result)