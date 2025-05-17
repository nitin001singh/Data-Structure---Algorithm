# Given a Tree of N Nodes, rooted at node 1 find the maximum sum of subtree possible.
# 
def DFS(node, G, used, parent, sum):
    used[node] = 1

    for u in G[node]:
        if used[u] == 0:
            parent[u] = node
            DFS(u, G, used, parent, sum)

    s = 0
    for child in G[node]:
        if child != parent[node]:
            s += sum[child]
            

    sum[node] = b[node] + s


if __name__ == "__main__":
    n = int(input( "Enter number of nodes : "))
    b = [0] * (n + 1)
    sum = [0] * (n + 1)
    G = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        b[i] = int(input(" Enter the weight : "))

    for _ in range(1,n):
        u, v = map(int, input(" Enter u and v space separated : ").split())
        G[u].append(v)
        G[v].append(u)

    used = [0] * (n + 1)
    parent = [0] * (n + 1)
    DFS(1, G, used, parent, sum)

    answer = float("-inf")
    for i in range(1, n + 1):
        answer = max(answer, sum[i])

    print(answer)
