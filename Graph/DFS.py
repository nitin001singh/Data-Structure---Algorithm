from queue import Queue

class Solution:
    def answer(self, n , m ):
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input("Enter space-separated x and y: ").split())
            graph[x].append(y)
            graph[y].append(x) 

        used = [0] * (n+1)
        parent = [0] * (n+1)
        self.dfs(1, graph, used, parent)
        
        
    def dfs(self, node , graph , used , parent):
        print(node)
        used[node] = 1
        
        for x in graph[node]:
            if used[x] == 0:
                parent[x] = node
                self.dfs(x, graph, used, parent)
        

n = 5
m = 4

result = Solution().answer(n, m)
print(result)