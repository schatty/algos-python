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


# Colors, 0 - white, 1 - gray, 2 - black
color = [-1] * (n + 1)
color_cnt = 2


for i in range(1, len(color)):
    # print("Node ", i, color[i])
    if color[i] != -1:
        continue

    stack = [i]
    while len(stack):
        v = stack.pop()
        if color[v] == -1:
            # Node is gray now
            color[v] = 0
            stack.append(v)

            if v in g:
                for v_out in g[v]:
                    if color[v_out] == -1:
                        stack.append(v_out)

        elif color[v] == 0:
            color[v] = color_cnt
            
    color_cnt += 1

# print("color", color)
# print("Cnt color", color_cnt)

print(color_cnt - 2)
for clr in range(2, color_cnt):
    clrs_tmp = []
    for i_node in range(1, len(color)):
        if color[i_node] == clr:
            clrs_tmp.append(i_node)
    print(*clrs_tmp)


