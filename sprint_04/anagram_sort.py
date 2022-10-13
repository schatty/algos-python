n = int(input())
sts = input().split()

mp = {}
for i, w in enumerate(sts):
    w_srt = tuple(sorted(w))
    if w_srt in mp:
        mp[w_srt].append(i)
    else:
        mp[w_srt] = [i]

# print(mp)

for k in sorted(mp, key = lambda x: mp[x][0]):
    print(*sorted(mp[k]))
    
