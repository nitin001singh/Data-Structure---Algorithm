from queue import Queue

class Solution:
    def answer(self):
        n = int(input("Enter number of nodes: "))
        m = int(input("Enter number of edges: "))
        
        matrix = [[] for _ in range(n)]
        
        for i in range(m):
            row, col = map(int, input("Enter space-separated x and y: ").split())
            matrix[row].append(col)
            matrix[col].append(row) 

        q = Queue()
        start_node = 0 
        q.put(start_node)

        used = [0] * n
        used[start_node] = 1

        level = [0] * n
        
        print("Node -> Level")
        while not q.empty():
            x = q.get()
            print(f"{x} -> {level[x]}")
            
            for y in matrix[x]:
                if used[y] == 0:
                    q.put(y)
                    used[y] = 1
                    level[y] = level[x] + 1

        return level 

# Run
result = Solution().answer()

print(result)