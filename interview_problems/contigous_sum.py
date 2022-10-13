"""
Find subsequence of the given sequence which sum is equal to K

How to solve: use the trick with hash of prefix sums.
"""

def find_sum(l, k):
    hsh = {0: 0}
    cum_sum = 0
    for i in range(len(l)):
        cum_sum += l[i]
        if cum_sum - k in hsh:
            return l[hsh[cum_sum - k]+1:i+1]
        hsh[cum_sum] = i 



l = [1, 0, 3, 5, 2, 14, 3]
print(find_sum(l, 10))
print(find_sum(l, 16))
