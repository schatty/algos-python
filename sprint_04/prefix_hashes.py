a = int(input())
m = int(input())
st = input()
t = int(input())

L = len(st)
hash_intervals = []
prev_lr = 0
for i in range(len(st)):
    hash_intervals.append((prev_lr * a + ord(st[i])) % m)
    prev_lr = hash_intervals[-1]


print("HASH INTERVALS 1: ", hash_intervals)

for _ in range(t):
    i, j = input().split()
    i, j = int(i) - 1, int(j) - 1
    l = j - i 
    
    if i > 0:
        hash_tmp = hash_intervals[j] - (hash_intervals[i - 1] * a ** (j - i + 1)) % m
    else:
        hash_tmp = hash_intervals[j]

    if hash_tmp < 0:
        hash_tmp = m + hash_tmp

    print(hash_tmp)

