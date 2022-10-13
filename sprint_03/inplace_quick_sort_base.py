def quick_sort(a, left_init, right_init):
    if right_init - left_init < 2:
        # print("base case", right_init, left_init, " els (", a[left_init], a[right_init], ")")
        if right_init - left_init == 1 and a[left_init] > a[right_init]:
            # print("Permuting!")
            a[left_init], a[right_init] = a[right_init], a[left_init]
            # print("array after: ", a)
        # print("returning with ", left_init, right_init)
        return

    pivot = right_init
    # print("Pivot element: ", a[pivot])

    left = left_init
    while left < pivot - 1:
        while left < pivot - 1 and a[left] <= a[pivot]:
            left += 1
        # while right > left + 1 and a[right] > pivot:
        #     right -= 1

        
        # print("before swith l p r", left, pivot, right, "vals (", a[left], a[pivot], a[right], ")")
        # print("a before: ", a)
        if a[left] > a[pivot]:

            # print("switching pivots", pivot, pivot - 1, "elements (", a[pivot], a[pivot - 1])
            # a[pivot - 1], a[pivot] = a[pivot], a[pivot - 1]
            # print("switching l r", left, right, " elements (", a[left], a[right] , ")")
            a[left], a[pivot] = a[pivot], a[left]

            pivot -= 1

        # print("a", a)
        # print()
    
    # _ = input("stop")
 
    # print("Launching qick sort for ", left_init, pivot - 1)
    quick_sort(a, left_init, pivot - 1)

    # print("Launching quick sort for ", pivot+1, right_init)
    quick_sort(a, pivot+1, right_init)


from random import randint
for _ in range(100):
    a = [randint(0, 1000) for _ in range(100)]
    qs = quick_sort(a, 0, len(a) - 1)
    qs == list(sorted(a)), "Bad case for", a, qs


# print("result: ", a)
