def find_pattern_shift():
    n = int(input())
    s = list(map(int, input().split()))
    m = int(input())
    p = list(map(int, input().split()))

    for i in range(n - 1):
        s[i] -= s[i + 1]
    s.pop()
    for i in range(m - 1):
        p[i] -= p[i + 1]
    p.pop()

    inds = []
    for i in range(n - m + 1):
        if s[i:i+m-1] == p:
            inds.append(i)

    return [x + 1 for x in inds]


print(*find_pattern_shift())
