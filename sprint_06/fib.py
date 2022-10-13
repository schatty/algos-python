n = int(input())

def calc_fib(n):
    limit = 10**9 + 7

    if n == 0:
        return 1
    if n == 1:
        return 1

    v_prev = 1
    v = 1

    for _ in range(1, n):
        tmp = v
        v = v_prev + v
        v_prev = tmp

        if v > limit:
            v %= limit

    return v


print(calc_fib(n))

