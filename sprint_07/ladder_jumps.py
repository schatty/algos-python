n, k = map(int, input().split())

l = [0] * n
l[0] = 1
l[1] = 1

lim = 10**9 + 7

for i in range(2, n):
    for j in range(1, min(k, i) + 1):
        l[i] += l[i-j]
    if l[i] > lim:
        l[i] %= lim

print(l[-1])
