# Brute Force 
# TC : O(N^2)
# SC : O(N^2)

# class Solution:
#     def answer(self , matrix):
#         n = len(matrix)
#         resp = [ [ 0 for _ in range(n)] for _ in range(n) ]
        
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])): 
#                 resp[col][n-row-1] = matrix[row][col]
                
            
#         return resp
    
# result = Solution().answer([[1,2,3],[4,5,6],[7,8,9]])
# print(result)


# Optimal
# TC : O(N^2)
# SC : O(1)

class Solution:
    def answer(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix


result = Solution().answer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
