m = int(input())
k = int(input())
coins = list(map(int, input().split()))


def min_coins(a, value):
    # print("Min coins", value)
    if value == 0:
        return 0

    res = float("inf")
    for coin in a:
        if coin <= value:
            # print("Coin ", coin, " launching for c = ", value - coin)
            subres = min_coins(a, value - coin)
            if subres is not None and subres + 1 < res:
                res = subres + 1

    return res

print(min_coins(coins, m))
