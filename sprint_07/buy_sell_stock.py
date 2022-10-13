n = int(input())
stocks = list(map(int, input().split()))
buy_sell = []

stock_sum = 0

i = 0
while i < n:
    # Find local minima
    l = i
    while l < n - 1:
        if stocks[l] < stocks[l + 1]:
            break
        l += 1

    if l == n - 1:
        break

    # Find local maxima
    r = l + 1
    while r < n - 1:
        if stocks[r] > stocks[r + 1]:
            break
        r += 1

    # Save min-max in buffer
    buy_sell.append((stocks[l], stocks[r]))
    stock_sum += stocks[r] - stocks[l]

    if r == n - 1:
        break

    i = r + 1

print(buy_sell)
print(stock_sum)
