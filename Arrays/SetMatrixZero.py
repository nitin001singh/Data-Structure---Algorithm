# Brute Force 

# TC : O(m*n)
# SC : O(m+n)

# class Solution:
#     def answer(self , matrix):
#         rows = set()
#         cols = set()
        
#         for rowIndex in range(len(matrix)):
#             for colIndex in range(len(matrix[0])):
#                 if matrix[rowIndex][colIndex] == 0:
#                     rows.add(rowIndex)
#                     cols.add(colIndex)

#         for rowIndex in range(len(matrix)):
#             for colIndex in range(len(matrix[0])):
#                 if rowIndex in rows or colIndex in cols:
#                     matrix[rowIndex][colIndex] = 0

#         return matrix
                
# result = Solution().answer(  [[1,1,2,2],[3,4,0,2],[1,0,1,5]] )
# print(result)


# Optimal
# TC : O(m*n)
# SC : O(1)


class Solution:
    def answer(self , matrix):
        firstRow = False
        firstCol = False
        
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if matrix[rowIndex][colIndex] == 0:
                    if rowIndex == 0 :
                        firstRow = True
                    if colIndex == 0:
                        firstCol = True
                        
                    matrix[0][colIndex] = 0
                    matrix[rowIndex][0] = 0
                        
                        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
                    
        if firstRow:
            for index in range(len(matrix[0])):
                matrix[0][index] = 0
                
                
        if firstCol:
            for index in range(len(matrix)):
                matrix[index][0] = 0
            
        
        return matrix
    
                
result = Solution().answer( [[1,1,1],[1,0,1],[1,1,1]] )
print(result)