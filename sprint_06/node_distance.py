n, m = input().split()
n, m = int(n), int(m)

g = {}
start_nodes = set([i for i in range(1, n+1)])
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

    if v in start_nodes:
        start_nodes.remove(v)

start_node, end_node = input().split()
start_node, end_node = int(start_node), int(end_node)

queue = [start_node]

# Colors, 0 - white, 1 - gray, 2 - black
color = [0] * (n + 1)
trace = []
color[queue[0]] = 1
prev = {}

# print("Graph:", g)
queue_i = 0
find_path = False

while queue_i < len(queue):# or len(start_nodes):
    # if queue_i == len(queue):
    #     queue = [start_nodes.pop()]
    #     queue_i = 0

    node = queue[queue_i]
    queue_i += 1

    trace.append(node)
   
    if node not in g:
        break

    if node == end_node:
        find_path = True
        break

    for v in g[node]:
        if color[v] == 0:
            color[v] = 1
            queue.append(v)
            prev[v] = node

    color[node] = 2

if find_path:

    if end_node not in prev:
        print(0)
    else:
        node = prev[end_node]
        cnt = 1
        while node != start_node:
            node = prev[node]
            # print("<-", node)
            cnt += 1

        # print("Find path", find_path)
        # print("Trace", trace)
        # print("Len", cnt)
        print(cnt)
else:
    print(-1)

