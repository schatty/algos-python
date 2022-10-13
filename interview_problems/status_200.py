"""
You are given an array of natural numbers a_i. Find the number of such pairs
(a_i, a_j) that |a_i - a_j| % 200 = 0, i < j.

Solution:
    * Key to know: if |a_i - a_j| % 200 == 0 than a_i % 200 == a_j % 200 = 0
    * Idea: we will store the a_i % 200 in a hash table, than each bucket
      will contain n elements. To count number of pairs from each bucket we
      calculate (n-1) * n // 2
"""


n = int(input())
a = list(map(int, input().split()))

mem = {}
for i in range(n):
    el = a[i] % 200
    if el in mem:
        mem[el] += 1
    else:
        mem[el] = 1

print(mem)

n_pairs = 0
for v in mem.values():
    if v > 1:
        n_pairs += (v-1) * v // 2
print(n_pairs)
