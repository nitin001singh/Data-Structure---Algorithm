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

    height[node] = max_height + 1



n = int(input("Enter number of nodes: "))
G = [[] for _ in range(n + 1)]
height = [0] * (n + 1)
print(f"Enter {n-1} edges (u v):")
for _ in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

used = [0] * (n + 1)
parent = [0] * (n + 1)

DFS(1, G, used, parent, height)

for i in range(1, n + 1):
    print(f"Node {i}: {height[i] - 1}")
