ss = input()
ans = 0
hash_pos = {}

i = 0
for j in range(len(ss)):
    if ss[j] in hash_pos:
        i = max(i, hash_pos[ss[j]])

    ans = max(j - i + 1, ans)
    hash_pos[ss[j]] = j + 1

print(ans)
