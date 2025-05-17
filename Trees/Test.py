from queue import Queue
class Solution:
    # "Given a Tree of “N” nodes and N-1 edges ; rooted at node “1” ; print “N” integers ; where the ith integer prints the number of children of the ith node. Once this is done ; print all the leaves of the particular tree. "
    
    def answer(self):
        n = int(input("Enter number of nodes : "))
        tree = [[] for _ in range(n+1)]
        for _ in range(1,n):
            x, y = map(int, input("Enter x, y space separated : ").split())
            tree[x].append(y)
            tree[y].append(x)
            
        q = Queue()
        used = [0] * (n + 1)
        child = [0] * (n + 1)
        
        
        start_node = 1
        q.put(start_node)
        
        used[start_node] = 1
        
        while not q.empty():
            node = q.get()
            c = 0
            for ch in tree[node]:
                if used[ch] == 0:
                    q.put(ch)
                    c += 1
                    used[ch] = 1
            child[node] = c
            
            
        print("\nNumber of children for each node:")
        for i in range(1, n + 1):
            print(f"Node {i}: {child[i]}")
    
        print("\nLeaf Nodes : ")
        for i in range(1, n + 1):
            if child[i] == 0:
                print(f"Node {i}")
        
        
    #  "Google Interview Problem.-> Given a Tree of ‘N’ Nodes and ‘N-1’ Edges; rooted at Node-1 ; each node is assigned either 1 or 0 ; for each node “i” ; find the number of 1’s on the shortest path from node 1 to node “i” "
    
    def answer2(self):   
        n = int(input("Enter number of nodes: "))
        tree = [[] for _ in range(n+1)]
        for _ in range(1,n):
            x, y = map(int, input("Enter x, y space separated : ").split())
            tree[x].append(y)
            tree[y].append(x)
            
        
        b = [0] * (n +1)
        used = [0] * (n + 1)
        answer = [0] * (n + 1)
        start_node = 1
        
        
        print(f"Enter value 0 or 1 for each node from 1 to {n}:")
        for i in range(1, n + 1):
            b[i] = int(input("Enter value :"))
                
                
        q = Queue()
        q.put(start_node)
        
        used[start_node] = 1
        answer[start_node] = b[start_node]
        
        while not q.empty():
            
            node = q.get()
            for child in tree[node]:
                if used[child] == 0:
                    q.put(child)
                    used[child] = 1
                    answer[child] = answer[node] + b[child]
                    
                    
        print("\nNumber of 1's on the path from node 1 to each node:")
        for i in range(1, n + 1):
            print(f"Node {i}: {answer[i]}")             
                
            
   #  "Given a Tree of “N” nodes; find the height of each node and print it ; the tree is rooted at Node-1. "   
        
    def answer3(self):   
        n = int(input("Enter number of nodes : "))
        tree = [ [] for _ in range(n+1) ]
        
        for _ in range(1, n):
            x, y = map(int , input("Enter value of x and y space separated : ").split())
            tree[x].append(y)
            tree[y].append(x)
        
        
        height = [0] * ( n + 1)
        used = [0] * ( n + 1)
        parent = [0] * ( n + 1)
        
        self.dfs(1, tree, used, parent, height)
        
        
        for i in range(1, n + 1):
            print(f"Node {i}: {height[i]}")
                    
            
            
    def dfs(self, node, tree, used, parent, height):
        used[node] = 1

        for child in tree[node]:
            if not used[child]:
                parent[child] = node
                self.dfs(child, tree, used, parent, height)

        max_height = 0
        for child in tree[node]:
            if child != parent[node]:
                max_height = max(max_height, height[child])

        height[node] = max_height + 1
        
        
# result = Solution().answer()
# result = Solution().answer2()
result = Solution().answer3()
print(result)

