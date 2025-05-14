# Given a Tree of “N” nodes; find the height of each node and print it ; the tree is rooted at Node-1. 
# 
def DFS(node, G, used, parent, height):
    used[node] = 1

    for child in G[node]:
        if not used[child]:
            parent[child] = node
            DFS(child, G, used, parent, height)

    max_height = 0
    for child in G[node]:
        if child != parent[node]:
            max_height = max(max_height, height[child])

    height[node] = 1 + max_height


n = int(input())
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

used = [0] * (n + 1)
parent = [0] * (n + 1)
height = [0] * (n + 1)

DFS(1, G, used, parent, height)

for i in range(1, n + 1):
    print(height[i] - 1)

