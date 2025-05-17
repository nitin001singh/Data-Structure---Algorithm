from queue import Queue

n = int(input("Enter number of nodes: "))
G = [[] for _ in range(n + 1)]

for _ in range(1,n):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

q = Queue()
used = [0] * (n + 1)
child = [0] * (n + 1)

used[1] = 1
q.put(1)


while not q.empty():
    node = q.get()
    c = 0
    for u in G[node]:
        if used[u] == 0:
            c += 1
            used[u] = 1
            q.put(u)
    child[node] = c


print("\nNumber of children for each node:")
for i in range(1, n + 1):
    print(f"Node {i}: {child[i]}")

# Print leaf nodes
print("\nLeaf nodes:")
for i in range(1, n + 1):
    if child[i] == 0:
        print(i, end=' ')
