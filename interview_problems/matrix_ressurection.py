"""
Longest Increasing Path in Matrix

Given m x n integers matrix, return the length of the longest increasing path
in matrix. For each cell, you can either move in four directions: left, right,
up, down. You can't move diagonally or outside the boundary.

Solution:
    * Idea: we combine the dynamic programmin with recursive DFS. We keep DP
      matrix with longest path for each (i, j). We will update the (i, j) as
      max(1, 1 + DFS(right), 1 + DFS(left), 1 + DFS(up), 1 + DFS(down). The 
      DFS will return 0 if the current value is smaller or equal to the
      value from which we came and DP[(i, j)] if such value has been already
      calculated.
"""


n, m = map(int, input().split())

mm = []
for _ in range(n):
    mm.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]

def dfs(i, j, prev_val):
    if (i < 0 or i == n or
        j < 0 or j == m or
        mm[i][j] <= prev_val):
        return 0

    if dp[i][j] > 0:
        return dp[i][j]

    val = mm[i][j]
    res = 1
    res = max(res, 1 + dfs(i - 1, j, val))
    res = max(res, 1 + dfs(i + 1, j, val))
    res = max(res, 1 + dfs(i, j - 1, val))
    res = max(res, 1 + dfs(i, j + 1, val))
    
    return res


max_val = -float('inf')
for i in range(n):
    for j in range(m):
        val = dfs(i, j, -1)
        dp[i][j] = val
        max_val = max(val, max_val)

# for i in range(n):
#     print(*mm[i])

print(max_val)


