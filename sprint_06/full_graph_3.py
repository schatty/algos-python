n, m = input().split()
n, m = int(n), int(m)

def solution_bignumbers(n, m):
    mm_u = [0] * n #[[0] * (n-1) for n in range(n, 1, -1)]
    mm_v = [0] * n
    for _ in range(m):
        u, v = input().split()
        u, v = int(u) - 1, int(v) - 1

        if u == v:
            continue

        # u should be less than v
        if u > v:
            u, v = v, u
        
        mm_u[u] += 1
        mm_v[v] += 1

    for i in range(n):
        if mm_u[i] + mm_v[i] < n - 1:
            print("NO")
            break
    else:
        print("YES")

def solution_smallnumbers(n, m):
    n, m = input().split()
    n, m = int(n), int(m)

    n -= 1

    l = n * (n + 1) // 2

    mm = [0] * l #[[0] * (n-1) for n in range(n, 1, -1)]
    for _ in range(m):
        u, v = input().split()
        u, v = int(u) - 1, int(v) - 1

        if u == v:
            continue

        # u should be less than v
        if u > v:
            u, v = v, u

        i_row = l - (n - u) * (n - u + 1) // 2

        mm[i_row + v - u - 1] = True

    for u in mm:
        if not u:
            print("NO")
            break
    else:
        print("YES")


if n < 50_000:
    solution_smallnumbers(n, m)
else:
    solution_bignumbers(n, m)
