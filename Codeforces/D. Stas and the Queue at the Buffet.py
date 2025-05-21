class Solution:
    def answer(self):
        n = int(input("Enter number of people : "))
        diff = []
        
        constantPart = 0
        for j in range(1,n+1):
            x , y = map(int, input("Enter space separated number : ").split())
            diff.append(  x - y  )
            constantPart += (y * n) - x
            

        diff.sort(reverse=True)
        
        variable_part = 0
        for i in range(n):
            variable_part += (i + 1) * diff[i]

        total_dissatisfaction = variable_part + constantPart
        return total_dissatisfaction
    
    
result = Solution().answer()
print(result)
