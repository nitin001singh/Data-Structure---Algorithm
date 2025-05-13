# Number of shortest paths from the source node to all other nodes

from queue import Queue

class Solution:
    def answer(self, n, m, start_node):
        matrix = [[] for _ in range(n + 1)]
        for i in range(m):
            x, y = map(int, input("Enter space-separated x and y: ").split())
            matrix[x].append(y)
            matrix[y].append(x)

        q = Queue()
        q.put(start_node)

        used = [0] * (n + 1)
        level = [-1] * (n + 1)
        ways = [0] * (n + 1)

        level[start_node] = 0
        used[start_node] = 1
        ways[start_node] = 1

        while not q.empty():
            x = q.get()
            for y in matrix[x]:
                if level[y] == -1:
                    level[y] = level[x] + 1
                    ways[y] = ways[x]
                    q.put(y)
                    
                elif level[y] == level[x] + 1:
                    ways[y] += ways[x]

        for i in range(1, n + 1):
            print(f"Node {i}: {ways[i]} shortest path(s)")

# Example Run
# Input edges: 1-2, 2-3, 2-4, 3-5
result = Solution().answer(5, 4, 1)
