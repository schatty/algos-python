n, budget = list(map(int, input().split()))
houses = list(map(int, input().split()))

houses.sort()

price_cum = 0
bought = 0
for house_price in houses:
    if price_cum + house_price <= budget:
        bought += 1
        price_cum += house_price

print(bought)
