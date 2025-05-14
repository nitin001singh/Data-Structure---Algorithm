from queue import Queue

n = int(input("Enter number of nodes: "))

b = [0] * (n + 1)
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

print(f"Enter value 0 or 1 for each node from 1 to {n}:")
for i in range(1, n + 1):
    b[i] = int(input())

q = Queue()
used = [0] * (n + 1)
answer = [0] * (n + 1)

used[1] = 1
answer[1] = b[1]
q.put(1)

while not q.empty():
    top = q.get()

    for u in G[top]:
        if not used[u]:
            used[u] = 1
            q.put(u)
            answer[u] = answer[top] + b[u]


print("\nNumber of 1's on the path from node 1 to each node:")
for i in range(1, n + 1):
    print(f"Node {i}: {answer[i]}")
