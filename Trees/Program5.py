from collections import defaultdict
def find_valid_binary_tree_root(n, edges):

    # Step 1: Build the adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Step 2: Look for a node with degree <= 2
    for node in range(1, n + 1):
        if len(adj[node]) <= 2:
            print("Valid root found (degree <= 2):", node)
            return node

    # Step 3: Fallback - Pick any leaf node (degree == 1)
    for node in range(1, n + 1):
        if len(adj[node]) == 1:
            print("Fallback root (leaf node):", node)
            return node

    # Step 4: If not found (should never happen in valid tree)
    print("No valid root found.")
    return -1


# ---------- Example Usage ----------

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    print(f"Enter {n - 1} edges (space-separated u v):")
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    root = find_valid_binary_tree_root(n, edges)
