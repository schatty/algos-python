n, m = input().split()
n, m = int(n), int(m)

g = {}
start_nodes = set(range(1, n + 1))
for _ in range(m):
    u, v = input().split()
    u, v = int(u), int(v)

    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)

    if v in start_nodes:
        start_nodes.remove(v)

stack = [start_nodes.pop()]

# Colors, 0 - white, 1 - gray, 2 - black
color = [0] * (n + 1)
order = []

while len(stack) or len(start_nodes):
    if len(stack) == 0:
        stack.append(start_nodes.pop())

    v = stack.pop()
    if color[v] == 0:

        # Node is gray now
        color[v] = 1
        stack.append(v)

        if v in g:
            for v_out in g[v]:
                if color[v_out] == 0:
                    stack.append(v_out)

    elif color[v] == 1:
        color[v] = 2
        order.append(v)

print(*order[::-1])

