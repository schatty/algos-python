n, M = map(int, input().split())
items = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(2)]

item = items[0]
for j in range(1, M + 1):
    if j < item:
        continue
    dp[0][j] = item

early_stop = False
for i in range(1, len(items)):
    i_row = i % 2
    i_row_prev = (i+1) % 2
    item = items[i]
    # print("item", item)
    for j in range(1, min(item, M)):
        # print(j)
        dp[i_row][j] = dp[i_row_prev][j]
    for j in range(item, M + 1):
        dp[i_row][j] = max(dp[i_row_prev][j], item + dp[i_row_prev][j - item])
    # print("LINE", i, " : ", dp[i])
    if dp[i_row][-1] == M:
        print(M)
        early_stop = True
        break

# for i in range(len(items)):
#     print(*dp[i])

if not early_stop:
    i_row = (len(items) - 1) % 2
    print(dp[i_row][-1])
        
