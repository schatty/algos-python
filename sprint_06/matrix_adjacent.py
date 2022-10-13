n, m = input().split()
n, m = int(n), int(m)

mm = [[0] * n for _ in range(n)]

for _ in range(m):
    i, j = input().split()
    i, j = int(i) - 1, int(j) - 1

    mm[i][j] = 1

for i in range(n):
    print(*mm[i])

