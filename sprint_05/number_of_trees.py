n = int(input())

def recursive_call(l):
    if len(l) <= 1:
        return 1

    ans = 0
    for i in range(len(l)):
        left = recursive_call(l[:i])
        right = recursive_call(l[i+1:])
        ans += left * right
    return ans


print(recursive_call(list(range(n))))
