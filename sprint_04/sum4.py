n = int(input())
s = int(input())
a = list(map(int, input().split()))

history = set()
n = len(a)
quads = set()

# a.sort()
# print("a", a)

pairs_hash = {}
for i in range(n):
    for j in range(i+1, n):
        pair_sum = a[i] + a[j]
        if pair_sum not in pairs_hash:
            pairs_hash[pair_sum] = [(i, j)]
        else:
            pairs_hash[pair_sum].append((i, j))

# print("Pairs hash: ", pairs_hash)

for i in range(n):
    for j in range(i + 1, n):
        # print("j", j)
        target = s - a[i] - a[j]
        # print("target", target)
        srch = pairs_hash.get(target)
        if srch is not None:
            for pair in srch:
                if i not in pair and j not in pair:
                    quads.add(tuple(sorted([a[i], a[j], a[pair[0]], a[pair[1]]])))
                    # print("Found: ", pair, a[i], a[j], "adding ", (i, j, pair[0], pair[1]), tuple(sorted([a[i], a[j], a[pair[0]], a[pair[1]]])))

    # txt = input("stop")


print(len(quads))
for q in sorted(quads):
    print(*q)
