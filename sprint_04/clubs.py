n = int(input())

clubs = {}
for _ in range(n):
    st = input()

    hash_val = ord(st[0]) + ord(st[-1])
    if hash_val not in clubs:
        clubs[hash_val] = [st]
        print(st)
    else:
        for c in clubs[hash_val]:
            if c == st:
                break
        else:
            clubs[hash_val].append(st)
            print(st)

# print(clubs.values())
