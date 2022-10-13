def insert_strings():
    s = input()
    n = int(input())

    words = {}
    for _ in range(n):
        w, pos = input().split()
        words[int(pos)] = w

    i = 0
    s_res = ''
    for k in sorted(words):
        while i < k:
            s_res += s[i]
            i += 1
        s_res += words[k]

    while i < len(s):
        s_res += s[i]
        i += 1

    return s_res


print(insert_strings())
