n, m = map(int, input().split())

g = {}
for _ in range(m):
    u, v = map(int, input().split())

    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)

    if v not in g:
        g[v] = [u]
    else:
        g[v].append(u)

            
def bfs_cycle(g, n):
    queue = [1]
    cnt = 0

    # Colors, 0 - white, 1 - gray, 2 - black
    colors = [None] * (n + 1)
    colors[queue[0]] = True

    queue_i = 0
    visited = set(range(1, n+1))

    # while queue_i < len(queue) or len(start_nodes):
    while cnt < n:
        if queue_i == len(queue):
            # for i in range(n, 0, -1):
            #     if colors[i] is None:
            #         queue = [i]
            #         break
            # else:
            #     return False

            if len(visited) == 0:
                return False
            queue = [visited.pop()]
            queue_i = 0
            colors[queue[0]] = True

        node = queue[queue_i]
        visited.remove(node)
        cnt += 1

        color = not colors[node]
        queue_i += 1
 
        if node not in g:
            continue

        for v in g[node]:
            if colors[v] is None:
                colors[v] = color
                queue.append(v)
            elif colors[v] == colors[node]:
                return True

    return False

if bfs_cycle(g, n):
    print("NO")
else:
    print("YES")
