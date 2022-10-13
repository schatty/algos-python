n, m = input().split()
n, m = int(n), int(m)

mm = [[0] * (n-1) for n in range(n, 1, -1)]
for _ in range(m):
    u, v = input().split()
    u, v = int(u) - 1, int(v) - 1

    if u == v:
        continue

    # u should be less than v
    if u > v:
        u, v = v, u

    mm[u][v - u - 1] = True

for i in range(n - 1):
    print(*mm[i])

break_cycle = False
for i in range(n - 1):
    for j in range(n - i - 1):
        if not mm[i][j]:
            print("NO")
            break_cycle = True
            break
    if break_cycle:
        break
else:
    print("YES")

