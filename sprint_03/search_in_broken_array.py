"""
https://contest.yandex.ru/contest/23815/run-report/69403202/

----------------------------- Idea ----------------------------

We treat an array as the concatenation of two increasing sequences
S1 and S2. If the target element is less than 0th element that it
belongs to S2 (as the first and smallest element of S1 is greater
than any from S2), otherwise - to S1. The main challenge is that the 
beginning of S2 is unknown yet. The algorithm has two steps:
    1. Find the splitting element between S1 and S2.
    2. Run binary search in the corresponding sequence.

How to find a splitting element? Given [left, right] interval from 
original array we can state that if the middle element is less than 
the left boundary means that the splitting happend in [left, middle]
subinterval, otherwise in the [middle, right] subinterval. As the middle
element halves the size of the original interval, we will need only log n
operations to find the splitting.

Implementation details:

    split - pointer that splits two increasing sequence and points 
            at the first element of the 2nd.

------------------------ Time Complexity ----------------------

Finding splitting element: O(log n)
Binary search: O(log n)

Total complexity: O(log n) + O(log n) = O(log n)

------------------------ Space Complexity ----------------------

O(n). We need only memory for array itself + auxiliary variables
supporing binary search.

"""

from bisect import bisect_left


def broken_search(nums, target):
    n = len(nums)

    # Find a splitting element O(log n)
    split = -1
    left = 0
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if mid == 0 or nums[mid] < nums[mid - 1]:
            split = mid
            break

        # Splitting is rightwards from the mid
        if nums[left] < nums[mid]:
            left = mid
        else:
            right = mid


    # Binary search on the known side O(log n)
    left = 0
    right = n
    if split > 0:
        if target < nums[left]:
            left = split
        else:
            right = split

    i = bisect_left(nums, target, lo=left, hi=right)
    if i != right and nums[i] == target:
        return i

    return -1

assert broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5) == 6
assert broken_search([5, 1], 1) == 1
assert broken_search([1], 1) == 0
assert broken_search([3, 5, 6, 7, 9, 1, 2], 4) == -1
assert broken_search([6, 7, 10, 0, 2, 4, 5], 3) == -1
assert broken_search([1, 5], 1) == 0
assert broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 50) == -1
assert broken_search([9, 1, 3, 8], 8) == 3
assert broken_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], 1) == 0
assert broken_search([12, 41, 122, 411, 412, 1222, 3000, 12222, 122222], 3000) == 6
