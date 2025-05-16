from queue import Queue
class Solution:
    # "Given a Tree of “N” nodes and N-1 edges ; rooted at node “1” ; print “N” integers ; where the ith integer prints the number of children of the ith node. Once this is done ; print all the leaves of the particular tree. "
    
    def answer(self):
        n = int(input("Enter number of nodes : "))
        tree = [[] for _ in range(n+1)]
        
        for _ in range(n-1):
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
        
        
result = Solution().answer()
print(result)