def merge(arr, lf, mid, rg):
    arr_sorted = [0] * (rg - lf)
    p1 = lf
    p2 = mid
    p3 = 0

    while p1 != mid and p2 != rg:
        if arr[p1] <= arr[p2]:
            arr_sorted[p3] = arr[p1]
            p1 += 1
            p3 += 1
        else:
            arr_sorted[p3] = arr[p2]
            p2 += 1
            p3 += 1

    if p1 == mid:
        while p3 != len(arr_sorted):
            arr_sorted[p3] = arr[p2]
            p2 += 1
            p3 += 1
    
    if p2 == rg:
        while p3 != len(arr_sorted):
            arr_sorted[p3] = arr[p1]
            p1 += 1
            p3 += 1

    return arr_sorted


def merge_sort(arr, lf, rg):
    if rg - lf == 1:
        return

    mid = lf + (rg - lf) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    for i, el in enumerate(merge(arr, lf, mid, rg)):
        arr[lf+i] = el


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

