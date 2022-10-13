n, m = input().split()
n, m = int(n), int(m)

n -= 1

l = n * (n + 1) // 2
print("l", l)

mm = [0] * l #[[0] * (n-1) for n in range(n, 1, -1)]
for _ in range(m):
    u, v = input().split()
    u, v = int(u) - 1, int(v) - 1

    if u == v:
        continue

    # u should be less than v
    if u > v:
        u, v = v, u

    print("u", u)
    i_row = l - (n - u) * (n - u + 1) // 2
    print("i_row", i_row)
    print("index", i_row + v - u - 1)

    mm[i_row + v - u - 1] = True

print(*mm)

break_cycle = False
for u in mm:
    if not u:
        print("NO")
        break
else:
    print("YES")

