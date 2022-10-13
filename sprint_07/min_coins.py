m = int(input())
k = int(input())
coins = list(map(int, input().split()))


dp = [float("inf") for _ in range(m + 1)]
dp[0] = 0

for i in range(m+1):
    for coin in coins:
        if coin > i:
            continue
        if dp[i - coin] + 1 < dp[i]:
            dp[i] = dp[i - coin] + 1

print(dp[-1])
