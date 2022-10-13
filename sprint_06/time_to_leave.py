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

for node in g:
    g[node].sort(reverse=True)

stack = [1]

# Colors, 0 - white, 1 - gray, 2 - black
color = [0] * (n + 1)
trace = []

time = -1
entry = [0] * (n + 1)
leave = [0] * (n + 1)

while len(stack):
    v = stack.pop()
    if color[v] == 0:
        time += 1
        entry[v] = time
        trace.append(v)

        # Node is gray now
        color[v] = 1
        stack.append(v)

        if v in g:
            for v_out in g[v]:
                if color[v_out] == 0:
                    stack.append(v_out)

    elif color[v] == 1:
        time += 1
        color[v] = 2
        leave[v] = time

for i in range(1, n+1):
    print(entry[i], leave[i])

