n, m = input().split()
n, m = int(n), int(m)

g = {}
# start_nodes = set([i for i in range(1, n+1)])
for _ in range(m):
    u, v = input().split()
    u, v = int(u), int(v)

    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)

    if v not in g:
        g[v] = [u]
    else:
        g[v].append(u)

    # if v in start_nodes:
    #     start_nodes.remove(v)

for node in g:
    g[node].sort()

start_node = int(input())
queue = [start_node]

# Colors, 0 - white, 1 - gray, 2 - black
color = [0] * (n + 1)
distances = [0] * (n+1)
trace = []

color[queue[0]] = 1

queue_i = 0

while queue_i < len(queue):# or len(start_nodes):
    node = queue[queue_i]
    queue_i += 1

    trace.append(node)
   
    if node not in g:
        break
    for v in g[node]:
        if color[v] == 0:
            color[v] = 1
            distances[v] = distances[node] + 1
            queue.append(v)

    color[node] = 2

print(max(distances))


