"""
We have `n` cards in a row on a table. During each move we can pick the card
from one of the ends. We can pick `k` cards. The final score is the sum of
picked cards. Determine the maximum possible score.


Idea: we can slide the window from the left moving in to the right across the
"gap" calculating the scores. We need only linear time of `k` to calculate
each possible sum. Then we return the maximum.
"""

n = int(input())
k = int(input())
a = list(map(int, input().split()))

def calc_max_sum(n, k, a):
    max_sum = sum(a[:k])
    cur_sum = max_sum
    for i in range(1, k + 1):
        cur_sum = cur_sum - a[k-i] + a[-i]
        max_sum = max(max_sum, cur_sum)

    return max_sum

print(calc_max_sum(n, k, a))
    
