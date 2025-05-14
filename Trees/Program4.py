# Given a Tree of N Nodes, rooted at node 1 find the maximum sum of subtree possible.
# 

def DFS(node, G, used, parent, subtree_sum, b):
    used[node] = 1

    for child in G[node]:
        if not used[child]:
            parent[child] = node
            DFS(child, G, used, parent, subtree_sum, b)

    total = 0
    for child in G[node]:
        if child != parent[node]:
            total += subtree_sum[child]

    subtree_sum[node] = b[node] + total


if __name__ == "__main__":
    n = int(input())

    b = [0] * (n + 1)  # Node values (1-based indexing)
    for i in range(1, n + 1):
        b[i] = int(input())

    G = [[] for _ in range(n + 1)]  # Adjacency list
    for _ in range(n - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    used = [0] * (n + 1)
    parent = [0] * (n + 1)
    subtree_sum = [0] * (n + 1)

    # Run DFS to compute subtree sums
    DFS(1, G, used, parent, subtree_sum, b)

    # Find the maximum subtree sum
    max_sum = max(subtree_sum[1:])
    print(max_sum)
