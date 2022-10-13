n = int(input())
num_coins = int(input())
coins = list(map(int, input().split()))

dp = [[0] * num_coins for _ in range(n + 1)]
for j in range(num_coins):
    dp[0][j] = 1


for i in range(1, n + 1):
    for j in range(num_coins):
        if j > 0:
            dp[i][j] += dp[i][j-1]
        if i - coins[j] >= 0:
            dp[i][j] += dp[i-coins[j]][j]

# for i in range(n + 1):
#     print(*dp[i])

print(dp[-1][-1])
