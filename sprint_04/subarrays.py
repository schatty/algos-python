n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

M = int(1e9 + 9) #9007
p = 3

p_pws = [1]
for _ in range(min(len(a1), len(a2))):
    p_pws.append(p_pws[-1] * p)


def compute_hash(a):
    h = 0
    for num in a:
        h = (h * p + num) % M
    return h


def rolling_hash(cur_hash, st_len, prv, nxt):
   new_hash = ((cur_hash - prv * p_pws[st_len - 1]) * p + nxt) % M
   return new_hash


def foo(l):
    sub_a1 = {}

    hash_roll = compute_hash(a1[:l])
    sub_a1[hash_roll] = [(0, l)]
    for i in range(1, n - l + 1):
        hash_roll = rolling_hash(hash_roll, l, a1[i-1], a1[i+l-1])
        if hash_roll not in sub_a1:
            sub_a1[hash_roll] = [(i, i+l)]
        else:
            sub_a1[hash_roll].append((i, i+l))


    hash_roll = compute_hash(a2[:l])
    if hash_roll in sub_a1:
        for el in sub_a1[hash_roll]:
            if a1[el[0]:el[1]] == a2[:l]:
                return l

    for i in range(1, m - l + 1):
        hash_roll = rolling_hash(hash_roll, l, a2[i-1], a2[i+l-1])
        if hash_roll in sub_a1:
            for el in sub_a1[hash_roll]:
                if a1[el[0]:el[1]] == a2[i:i+l]:
                    return l
    return 0

def binary_search():
    if len(a1) == 1 or len(a2) == 1:
        if len(a1) == 1 and a1[0] in a2:
            return 1
        elif len(a2) == 1 and a2[0] in a1:
            return 1
        else:
            return 0
              
    l, r = 0, min(len(a1), len(a2))
    while l <= r:
        mid = l + (r - l) // 2
        if foo(mid):
            l = mid + 1
        else:
            r = mid - 1

    if l <= 0: return 1
    return l - 1

print(binary_search())


