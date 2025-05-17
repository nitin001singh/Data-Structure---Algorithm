# https://www.desiqna.in/12818/vmware-sde1-coding-questions-and-solutions-india-april-2023 

def DFS(node, G, used, parent, sum_values):
    used[node] = 1

    for u in G[node]:
        if used[u] == 0:
            parent[u] = node
            DFS(u, G, used, parent, sum_values)

    s = 0
    for child in G[node]:
        if child != parent[node]:
            s = max(s, sum_values[child])

    sum_values[node] = b[node] + s


n = int(input("Enter number of node : "))
sum_values = [0] * (n + 1)
b = [0] * (n + 1)
G = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    b[i] = int(input("Enter arr value "))

for _ in range(1, n):
    u, v = map(int, input("Enter space separated u and v : ").split())
    G[u].append(v)
    G[v].append(u)

used = [0] * (n + 1)
parent = [0] * (n + 1)
DFS(1, G, used, parent, sum_values)

answer = float("-inf")
for i in range(1, n + 1):
    answer = max(answer, sum_values[i])

print(answer)
