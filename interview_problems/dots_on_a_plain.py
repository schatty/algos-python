def solution():
    n = int(input())

    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    if n == 2:
        print("YES")
        return

    denom_zero = False
    if y0 - y1 == 0:
        denom_zero = True
        ratio = float("inf")
    else:
        ratio = (x0 - x1) / (y0 - y1)
        ratio = round(ratio, 5)

    for _ in range(2, n):
        x, y = map(int, input().split())
       
        if y1 - y == 0:
            if not denom_zero:
                print("NO")
                return
        else: 
            new_ratio = round((x1 - x) / (y1 - y), 5)
            if ratio != new_ratio:
                print("NO")
                return

        x1 = x
        y1 = y

    print("YES")

solution()
