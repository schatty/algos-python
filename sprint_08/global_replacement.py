def calc_prefix(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        pi[i] = k

    return pi

def replace():
    s = input()
    source = input()
    rep = input()

    if len(source) > len(s):
        return s

    s = source + "#" + s
    prefix = calc_prefix(s)
    inds = []
    for i, p in enumerate(prefix[len(source)+1:], start=len(source)+1):
        if p == len(source):
            inds.append(i - len(source))

    if len(inds) == 0:
        return s[len(source)+1:]

    print(prefix)
    print(inds)

    s_res = ""
    i_prev = len(source) + 1
    for idx in inds:
        print("Appending from orig: ", s[i_prev:idx], idx, i_prev)
        s_res += s[i_prev:idx+1] + rep
        i_prev = idx + 1 + len(source)

    print("String so far: ", s_res)
    print("Adding: ", s[inds[-1]+1+len(source):])
    s_res += s[inds[-1]+1+len(source):]


    return s_res

print()
print(replace())
