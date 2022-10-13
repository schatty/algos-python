'''
N-Queens Problem

Determine all possible combination of queens on a desk such that queens can't
beat each other.

Solution:
    * Key to know #1: Two cells are at the same diagonal if they have the same 
      difference between i-th and j-th indices.
    * Backtracking approach.
'''

n = int(input())

res = 0
cols = []
pos_diag = set()
neg_diag = set()
tracks = []

def backtrack(row):
    global res, tracks

    if row == n:
        tracks.append([i + 1 for i in cols])
        res += 1
        return

    for col in range(n):
        if col in cols or col + row in pos_diag or row - col in neg_diag:
            continue

        cols.append(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        backtrack(row + 1)
        cols.pop()#.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)

backtrack(0)

print(res)
for track in tracks:
    print(*track)
