# For each node in the graph find if it's reachable or not from the source node 


from queue import Queue

class Solution:
    def answer(self, n, m, start_node):
        matrix = [[] for _ in range(n+1)]
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
        
        while not q.empty():
            x = q.get()
            print(f"{x} -> {level[x]}")
            
            for y in matrix[x]:
                if used[y] == 0:
                    q.put(y)
                    used[y] = 1
                    level[y] = level[x] + 1

        # return level 
        
        i = 1
        while i <= n:
            if used[i] == 0:
                print("you can not visit {} node from {} node".format(i, start_node))
            else:
                print("you can visit {} node from {} node".format(i, start_node))
            i += 1

# Run
result = Solution().answer(5,4, 1)
print(result)