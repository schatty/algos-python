n, m = input().split()
n, m = int(n), int(m)

g = {}
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

start_node = int(input())
stack = [start_node]

# Colors, 0 - white, 1 - gray, 2 - black
color = [0] * (n + 1)
trace = []

while len(stack):
    v = stack.pop()
    if color[v] == 0:
        trace.append(v)

        # Node is gray now
        color[v] = 1
        stack.append(v)

        if v in g:
            for v_out in sorted(g[v], reverse=True):
                if color[v_out] == 0:
                    stack.append(v_out)

    elif color[v] == 1:
        color[v] = 2


print(*trace)
