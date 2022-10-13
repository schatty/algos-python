# def less(i, j): 
#     """Returns if i-th element is bigger than j-th in lexographic order. """
#     if POINTS[i] < POINTS[j]:
#         return True
#     elif POINTS[i] == POINTS[j] and PENS[i] > PENS[j]:
#         return True
#     elif POINTS[i] == POINTS[j] and PENS[i] == PENS[j] and LOGINS[i] > LOGINS[j]:
#         return True
#     return False


# def subst(i, j):
#     POINTS[i], POINTS[j] = POINTS[j], POINTS[i]
#     PENS[i], PENS[j] = PENS[j], PENS[i]
#     LOGINS[i], LOGINS[j] = LOGINS[j], LOGINS[i]

def less(i, j):
    return POINTS[i] < POINTS[j]


def subst(i, j):
    POINTS[i], POINTS[j] = POINTS[j], POINTS[i]


def quick_sort(left_init, right_init):
    # print("START: ", POINTS) #, PENS, LOGINS)
    if right_init - left_init < 2:
        # print("base case", right_init, left_init, " els (", POINTS[left_init], POINTS[right_init], ")")
        if right_init - left_init == 1 and less(left_init, right_init):
            print("Base case!")
            # a[left_init], a[right_init] = a[right_init], a[left_init]
            subst(left_init, right_init)
            # print("a: ", POINTS, PENS, LOGINS)
        return

    pivot = left_init
    print("pivot right", pivot, right_init)

    right = right_init
    while right > pivot + 1:
        while right > pivot + 1 and less(right, pivot): #a[left] <= a[pivot]:
            right -= 1
            # print(f"Moving left l = {left} ({POINTS[left]}, {PENS[left]}, {LOGINS[left]})")
        
        if less(pivot, right):
            # print(f"Going to switch: {left} {pivot} ({POINTS[left]} {POINTS[pivot]}) ({LOGINS[left]} {LOGINS[pivot]})")

            # print(f"switching pivots {pivot}, {pivot - 1} ({POINTS[pivot]} {POINTS[pivot - 1]})")
            # a[pivot - 1], a[pivot] = a[pivot], a[pivot - 1]
            if right - pivot > 1:
                subst(pivot, pivot + 1)
            else:
                print("not performint pivot switch")
            # print("switching l r", left, pivot, " elements (", POINTS[left], POINTS[pivot] , ")")
            # a[left], a[pivot] = a[pivot], a[left]
            subst(pivot, right)

            pivot += 1
        else:
            print("not doing switch")

        # print("a", POINTS, PENS, LOGINS)
        print()

    if less(pivot, right):
        print("Perform last perm (r p)", right, pivot)
        subst(right, pivot)
        pivot += 1
        # print("a", POINTS, PENS, LOGINS)
    
    # _ = input("stop")
 
    print("REC L", left_init, pivot - 1)
    quick_sort(left_init, pivot - 1)

    print("REC R", pivot+1, right_init)
    quick_sort(pivot + 1, right_init)


from random import randint

for _ in range(100):
    POINTS = [randint(0, 1000) for _ in range(100)]
    quick_sort(0, len(POINTS) - 1)
    print("POINTS SORTED: ", POINTS)
    assert POINTS == list(sorted(POINTS, reverse=True)), f"Bad case for {POINTS}"
else:
    print("OK.")

# Case # 1

# LOGINS = ["alla", "gena", "gosha", "rita", "timofey"]
# POINTS = [4, 6, 2, 2, 4]
# PENS = [100, 1000, 90, 90, 80]

# Case # 2

# LOGINS = ["alla", "gena", "gosha", "rita", "timofey"]
# POINTS = [0] * 5
# PENS = [0] * 5

# n = int(input())
# LOGINS, POINTS, PENS = [], [], []
# for _ in range(n):
#     l = input().split()
#     LOGINS.append(l[0])
#     POINTS.append(int(l[1]))
#     PENS.append(int(l[2]))

# Test # 12

# LOGINS = ["ixetulueozem", "edrnkztanvrpyjvso", "e", "ayrcrulcwh", "nsgnysqm", "ewdponbpcmtgfabnvo", "sfkropatfwkna", "kzibjralr", "hnpmykspichx", "armaholwvkttg", "vswomwpuhpqzxstltlw"]
# POINTS = [55, 65, 89, 99, 15, 65, 95, 2, 34, 9, 10]
# PENS = [26, 7, 9, 14, 32, 15, 59, 12, 87, 47, 40]

# quick_sort(0, len(LOGINS) - 1)

# logins = LOGINS
# logins_true = ["ayrcrulcwh",
# "sfkropatfwkna",
# "e",
# "edrnkztanvrpyjvso",
# "ewdponbpcmtgfabnvo",
# "ixetulueozem",
# "hnpmykspichx",
# "nsgnysqm",
# "vswomwpuhpqzxstltlw",
# "armaholwvkttg",
# "kzibjralr"]
# assert logins == logins_true, f"Got {logins}"

print("LOGINS: ")
print(*LOGINS, sep="\n")
