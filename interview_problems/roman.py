s = input() + ' '

sym2num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    ' ': 0,
}
cnt = {sym: 0 for sym in "IXCMVLD"}
limits = {}
for sym in "IXCM":
    limits[sym] = 3
for sym in "VLD":
    limits[sym] = 1

i = 0
num = 0
skip = False
while i < len(s):
    sym = s[i]
    if sym in limits:
        cnt[sym] += 1
        # print("cnt", cnt)
        if cnt[sym] > limits[sym]:
            print(-1)
            break

    if skip:
        skip = False
    elif sym == 'I' and s[i+1] == 'V':
        num += 4
        skip = True
    elif sym == 'I' and s[i+1] == 'X':
        num += 9
        skip = True
    elif sym == 'X' and s[i+1] == 'L':
        num += 40
        skip = True
    elif sym == 'X' and s[i+1] == 'C':
        num += 90
        skip = True
    elif sym == 'C' and s[i+1] == 'D':
        num += 400
        skip = True
    elif sym == 'C' and s[i+1] == 'M':
        num += 900
        skip = True
    else:
        num += sym2num[sym]
        # print("SYM: ", sym, sym2num[sym])

    i += 1
else:
    print(num)
