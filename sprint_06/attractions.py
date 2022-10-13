n, m = input().split()
n, m = int(n), int(m)

g = {}
for _ in range(m):
    u, v, w = input().split()
    u, v, w = int(u), int(v), int(w)
    if u not in g:
        g[u] = {v: w}
    # for yandex special test
    elif v not in g[u]:
        g[u][v] = w
    if v not in g:
        g[v] = {u: w}
    # for yandex special test
    elif u not in g[v]:
        g[v][u] = w


def unvisited_nodes_left(dist, visited, node_from):
    for i in range(n):
        if dist[node_from - 1][i] != float("inf") and not visited[i]:
            return True
    return False


def get_min_dist_not_visited_vertex(visited, dist, node_from):
    cur_min = float("inf")
    cur_min_ver = -1

    for v in range(1, n + 1):
        if not visited[v - 1] and dist[node_from - 1][v - 1] < cur_min:
            cur_min = dist[node_from - 1][v - 1]
            cur_min_ver = v

    return cur_min_ver


def relax(dist, node_from, u, v):
    if dist[node_from - 1][v - 1] > dist[node_from - 1][u - 1] + g[u][v]:
        dist[node_from - 1][v - 1] = dist[node_from - 1][u - 1] + g[u][v]

 
dist = [[float("inf")] * n for _ in range(n)]
for i_node in range(1, n+1):
    visited = [False] * n
    dist[i_node - 1][i_node - 1] = 0
    
    while unvisited_nodes_left(dist, visited, i_node):
        u = get_min_dist_not_visited_vertex(visited, dist, i_node)
        print("Get node", u)
        visited[u - 1] = True

        if u not in g:
            continue

        neighbours = list(g[u].keys())
        print(u, " has neighbors ", neighbours)

        print("Before relaxation: ", dist[u - 1])
        for v in neighbours:
            relax(dist, i_node, u, v)
        print("After relaxation: ", dist[u - 1])

    # break


for i in range(n):
    print(*[x if x != float("inf") else -1 for x in dist[i]])


