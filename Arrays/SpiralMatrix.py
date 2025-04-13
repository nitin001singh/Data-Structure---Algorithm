
# Optimal 
# TC : O(m × n) 
# SC : O(m × n) 

class Solution:
    def answer(self, matrix):
        m , n = len(matrix) , len(matrix[0])
        ans = []
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        
        while top <= bottom and left <= right:
            # right
            
            for index in range(left, right+1):
                ans.append(matrix[top][index])
            
            top += 1
            
            #bottom
            
            for index in range(top, bottom+1):
                ans.append(matrix[index][right])
            
            right -= 1
            
            # right
            
            if top <= bottom:
            
                for index in range(right, left-1, -1):
                    ans.append(matrix[bottom][index])
                    
                    
                bottom -= 1
            
            
            # top
            
            if left <= right:
                    
                for index in range(bottom, top-1, -1):
                    ans.append(matrix[index][left])
                    
                left += 1
        
        return ans
    
# result = Solution().answer( [[1,2,3],[4,5,6],[7,8,9]] ) 
result = Solution().answer( [[1,2,3,4],[5,6,7,8],[9,10,11,12]] ) 
print(result)