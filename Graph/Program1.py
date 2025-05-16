# Take input of graph; then tell for each node “i” how many nodes are directly connected to it 


# Using Matrix 

# SC : O(N*N)

class Solution:
    def answer(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        
        matrix = [[0] for _ in range(n)]
        # return matrix
        
        for i in range(m):
            row , col = map(int, input("Enter space separated x and y : ").split())
            matrix[row][col] = 1
            matrix[col][row] = 1

            
            
        for x in range(n):
            count = 0
            for y in range(n):
                if matrix[x][y] == 1:
                    count += 1
                
                print("Count is :", count)
        
result = Solution().answer()
print(result)


# Using Adjacency List Representation   ( Array of arrays. )

# TC : O(N)
# SC : O(N+2*M) :-> O(N+M.)


class Solution:
    def answer(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        
        matrix = [[0] for _ in range(n)]
        # return matrix
        
        for i in range(m):
            row , col = map(int, input("Enter space separated x and y : ").split())
            matrix[row].append(col)
            matrix[col].append(row)
            
        for x in range(n):
            count = len(matrix[x])
            print("Count is :", count)
        
result = Solution().answer()
print(result)