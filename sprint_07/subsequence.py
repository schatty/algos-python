n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a1[i - 1] == a2[j - 1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print()
# for i in range(n + 1):
#     print(*dp[i])
ans = dp[-1][-1]
print(ans)

if ans:
    a1_path, a2_path = [], []
    i , j = n, m
    while i > 0 and j > 0:
        if a1[i-1] == a2[j-1]:
            a1_path.append(i)
            a2_path.append(j)
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    print(*a1_path[::-1])
    print(*a2_path[::-1])
