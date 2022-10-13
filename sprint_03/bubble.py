n = int(input())
a = list(map(int, input().split()))

shifted_once = False
for i in range(n - 1):
    shifted = False
    for j in range(1, n - i):
        if a[j-1] > a[j]:
            # print("ij" , i, j, "|", a[j], a[j-1])
            a[j-1], a[j] = a[j], a[j-1]
            shifted = True
    if shifted:
        print(*a)
        shifted_once = True

if not shifted_once:
    print(*a)
