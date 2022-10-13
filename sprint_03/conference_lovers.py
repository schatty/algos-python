n = int(input())
ids = list(map(int, input().split()))
k = int(input())

cnt = {}
for id_ in ids:
    if id_ in cnt:
        cnt[id_] += 1
    else:
        cnt[id_] = 1

cnt_sorted = {k: (v, k) for k, v in sorted(cnt.items(), key=lambda el: el[1], reverse=True)}
cnt_sorted = list(cnt_sorted.items())

print(*[tup[0] for tup in cnt_sorted[:k]])
