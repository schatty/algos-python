n = int(input())
a = list(map(int, input().split()))


def greater(x, y):
    """
    Returns true if x > y.
    """
    x_o, y_o = x, y

    x_f = x
    x_k = 0
    while x_f >= 10:
        x_k += 1
        x_f //= 10

    y_f = y
    y_k = 0
    while y_f >= 10:
        y_k += 1
        y_f //= 10

    if x_f > y_f:
        # print("base case > ", x_f, y_f)
        return True 
    elif x_f < y_f:
        # print("base case < ", x_f, y_f)
        return False


    # (1) Turn given numbers in 3-digit numbers
    if x_k == 0:
        x = x * 10 + x
    elif x_k == 1:
        x = (x * 10 + (x%10)) % 100
    else:
        x %= 100
    
    if y_k == 0:
        y = y * 10 + y
    elif y_k == 1:
        y = (y * 10 + (y%10)) % 100
    else:
        y %= 100


    # (2) Convert it to the sorting key
    x_m = (x // 10 - x_f) * 10 + ((x % 10) - x_f)
    y_m = (y // 10 - y_f) * 10 + ((y % 10) - y_f)

    # if x_o == 898:
    #     print("orig: ", x_o, y_o)
    #     print("x y", x, y)
    #     print("x_m, y_m", x_m, y_m)
    #     print()

    if x_m == y_m and x_o < y_o:
        if x_f > x_o % 10:
            return True
        else:
            return False
        # print("Equal case: ", x_m, y_m, " | ", x_o, y_o)

    return x_m > y_m
    


# left = 1000 / num
# if left > 100:
#     return num * 1000# + 999
# elif left > 10:
#     return num * 100# + 99
# return num * 10# + 9


# a = [key_func(x) for x in a]

# Insertion sort (<-)
for i in range(n - 1):
    for j in range(i+1, n):
        if greater(a[j], a[i]):
            a[i], a[j] = a[j], a[i]

print(''.join(map(str, a)))

print(a)
