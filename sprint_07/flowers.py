n, m = map(int, input().split())

mm = []
for i in range(n):
    mm.append(list(map(int, input())))

for i in range(n):
    print(*mm[i])

dp = []
for _ in range(n):
    dp.append([-float("inf")] + [0] * m)
dp.append([-float("inf")] * (m+1))

# dp[n - 1][0] = mm[n - 1][0]

for i in range(n - 1, -1, -1):
    for j in range(1, m + 1):
        if i == n - 1 and j == 1:
            dp[i][j] = mm[i][j - 1]
        else:
            dp[i][j] = mm[i][j - 1] + max(dp[i+1][j], dp[i][j - 1])

print()
for i in range(n + 1):
    print(*dp[i])

print(dp[0][-1])

