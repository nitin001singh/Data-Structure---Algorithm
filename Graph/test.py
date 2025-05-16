from queue import Queue
class Solution:
    
    # "Take input of graph; then tell for each node “i” how many nodes are directly connected to it "
    
    def answer(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1)]

        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            
            graph[x].append(y)
            graph[y].append(x)
            
        for x in range(n+1):            
            print(len(graph[x])) 
        
        
    # # BFS Implementation
    
    def answer1(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1)]
        
        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            graph[x].append(y)
            graph[y].append(x)
        
        q = Queue()
        used = [0] * (n + 1)
        level = [0] * (n + 1)
        
        start_node = 1
        q.put(start_node)
        
        used[start_node] = 1
        level[start_node] = 0
        
        while not q.empty():
            node = q.get()
            print(f"{node} -> {level[node]}")
            
            for child in graph[node]:
                if used[child] == 0:
                    q.put(child)
                    used[child] = 1
                    level[child] = level[node] + 1
                
        return level
                
            
    # Shortest distance from given source
    
    def answer2(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1) ]
        
        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            graph[x].append(y)
            graph[y].append(x)
        
        q = Queue()
        used = [0] * (n + 1)
        level = [0] * (n + 1)
        
        start_node = 1
        q.put(start_node)
        
        used[start_node] = 1
        level[start_node] = 0
        
        while not q.empty():
            node = q.get()
            print(f"{node} -> {level[node]}")
            
            for child in graph[node]:
                if used[child] == 0:
                    q.put(child)
                    used[child] = 1
                    level[child] = level[node] + 1
    
        i = 0
        while i <= n:
            print(level[i], end=" " )
            i = i + 1
            
        
    
    # For each node in the graph find if it's reachable or not from the source node 
    
    def answer3(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1) ]
        
        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            graph[x].append(y)
            graph[y].append(x)
        
        q = Queue()
        used = [0] * (n + 1)
        level = [0] * (n + 1)
        
        start_node = 1
        q.put(start_node)
        
        used[start_node] = 1
        level[start_node] = 0
        
        while not q.empty():
            node = q.get()
            print(f"{node} -> {level[node]}")
            
            for child in graph[node]:
                if used[child] == 0:
                    q.put(child)
                    used[child] = 1
                    level[child] = level[node] + 1
    
        i= 1
        while i <= n:
            if used[i] == 0:
                print(
                    'Reacable'
                )
            else:
                print("Not Reachable ")
            
            i += 1
            
            
    # Number of shortest paths from the source node to all other nodes
    
    def answer4(self):
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1) ]
        
        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            graph[x].append(y)
            graph[y].append(x)
        
        q = Queue()
        used = [0] * (n + 1)
        level = [0] * (n + 1)
        ways = [0] * (n + 1)
        
        start_node = 1
        q.put(start_node)
        
        used[start_node] = 1
        level[start_node] = 0
        ways[start_node] = 1
        
        while not q.empty():
            node = q.get()
            for child in graph[node]:
                if level[child] == 0:
                    q.put(child)
                    level[child] = level[node] + 1
                    ways[child] = ways[node]
                    
                elif level[child] == level[node] + 1:
                    ways[child] += ways[node]

        for i in range(1, n + 1):
            print(f"Node {i}: {ways[i]} shortest path(s)")
            
            
    # DFS implementation
    
    
    def dfs(self, node, graph, used, parent):
        print(node)
        used[node] = 1
        for x in graph[node]:
            if used[x] == 0:
                parent[x] = node
                self.dfs(x, graph, used, parent)
        
    
    def answer5(self):
        
        n = int(input("Enter number of nodes : "))
        m = int(input("Enter number of edges : "))
        graph = [ [] for _ in range(n+1) ]
        
        for _ in range(m):
            x, y = map(int, input("Enter value of x and y space separated : ").split())
            graph[x].append(y)
            graph[y].append(x)
        
        used = [0] * (n + 1)
        parent = [0] * (n + 1)
        
        self.dfs(1, graph, used, parent)
        
    
# result = Solution().answer()
# result = Solution().answer1()
# result = Solution().answer2()
# result = Solution().answer3()
# result = Solution().answer4()
result = Solution().answer5()
print(result)