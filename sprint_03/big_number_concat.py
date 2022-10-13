n = int(input())
a = list(map(int, input().split()))


def greater(x, y):
    """
    Returns true if x > y.
    """
    x_g = int(str(x) + str(y))
    y_g = int(str(y) + str(x))

    return x_g > y_g
    


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
