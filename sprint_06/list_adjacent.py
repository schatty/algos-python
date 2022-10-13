n, m = input().split()
n, m = int(n), int(m)

nodes = {}
for i in range(m):
    u, v = input().split()
    u, v = int(u), int(v)

    if u not in nodes:
        nodes[u] = [v]
    else:
        nodes[u].append(v)


for node in range(1, n + 1):
    if node in nodes:
        print(len(nodes[node]), *sorted(nodes[node]))
    else:
        print(0)
