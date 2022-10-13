"""
Given array for each element find a number of elements from the left
that are less then the current element.
"""

def calc_left_less(a):
    ans = [0] * len(a)
    for i in range(1, len(a)):
        cnt = 0
        for j in range(i):
            if a[j] < a[i]:
                cnt += 1
        ans[i] = cnt

    print(ans)

    return ans


def test():
    assert calc_left_less([2, 3, 8, 5, 9]) == [0, 1, 2, 1, 4]
    print("OK.")

test()
