from queue import Queue

class Solution:
    def answer(self, n , m , start_node):
        matrix = [[] for _ in range(n + 1)]
        
        for i in range(m):
            x, y = map(int, input("Enter space-separated x and y: ").split())
            matrix[x].append(y)
            matrix[y].append(x) 

        q = Queue()
        q.put(start_node)

        used = [0] * (n+1)
        level = [0] * (n+1)
        
        used[start_node] = 1
        level[start_node] = 0

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
n = 5
m = 4
start_node = 1
result = Solution().answer(n, m, start_node)

print(result)