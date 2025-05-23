# TC : O(M + N)
# SC : O(N)

class Solution:
    def answer(self):
        n = int(input("Enter the number of elements : "))
        
        s1 = []
        s2 = []
        for _ in range(n):
            s1.append(input("Enter string in first string list : "))
        
        for _ in range(n):
            s2.append(input("Enter string in second string list : "))  
            
            
        for i in range(n):
            if self.check(s1[i], s2[i]):
                print('Yes')
            else:
                print("No")
            print()
            
            
    def check(self , s1, s2):
        s1_even = {}
        s1_odd = {}
        s2_even = {}
        s2_odd = {}
        for i in range(len(s1)):
            if i % 2 == 0:
                s1_even[s1[i]] =  s1_even.get(s1[i], 0) +  1
            else:
                s1_odd[s1[i]] = s1_odd.get(s1[i], 0) +  1
        
        for j in range(len(s2)):
            if j % 2 == 0:
                s2_even[s2[j]] = s2_even.get(s2[j], 0) +  1
            else:
                s2_odd[s2[j]] = s2_odd.get(s2[j], 0) +  1
            
            
        if s1_even == s2_even and s1_odd == s2_odd:
            return True
        
        return False
            
            
result = Solution().answer()
# print(result)