"""
https://contest.yandex.ru/contest/23815/run-report/69403079/

----------------------------- Idea ----------------------------

In-place QuickSort algorithm with specific comparing and substutining
functions.

Stage 1: Switching elements around the pivot.

Idea: move two pointers form the end of an array. Left pointer will
move until it points at the element bigger than pivot. Right pointer
will move until it points at the element less than pivot. Switch those
elements and proceed moving pointer until they reach the pivot.

Stage 2: Recursion.

Run 2 recrusion function, one for all the elements positioned leftwards
from the pivot, the other for all the element positioned rightwards from
the pivot.

------------------------ Time Complexity ----------------------

O(n logn m) as we need approximately logn recursion calls within
which we will perform n operations of switching and comparing. The worst
case for comparison operation
    * O(1) for point comparison
    * O(1) for penalty comparison
    * O(m), where m is the length of the minimal string for lexicographic
      comparison

------------------------ Space Complexity ----------------------

O(n). We need only memory for array(s) itself and 5 additional variables:
    left - points to the left boundary of processing array area.
    right - points to the right boundary of processing array area.
    lp (left pointer) - points to the current pointer from the left.
    rp (right pointer) - points to the current pointer from the right.
    pivot - central element around which we switch elements.


"""

def less(i, j): 
    """
    Returns if i-th element is less than j-th in lexographic order. 

    Note, we use "greater" operator + negative points values because
    of the problem formulation (we want reverse lexigraphic order for 
    string).
    """
    return DATA[i] > DATA[j]


def subst(i, j):
    """Substitutes i-th element with j-th. """
    DATA[i], DATA[j] = DATA[j], DATA[i]


def quick_sort(left, right, right_limit):
    if right <= 0 or left >= right_limit or right - left <= 0:
        return

    pivot = left + (right - left) // 2
    lp, rp = left, right
    while lp < rp:
        while lp < pivot and less(lp, pivot):
            lp += 1
        while rp > pivot and not less(rp, pivot):
            rp -= 1

        if lp < rp:
            subst(lp, rp)
            if pivot == lp:
                pivot = rp
            elif pivot == rp:
                pivot = lp

    quick_sort(left, pivot - 1, right_limit)
    quick_sort(pivot + 1, right, right_limit)


n = int(input())
DATA = []
for _ in range(n):
    login, point, pen = input().split()
    DATA.append((-int(point), int(pen), login))

quick_sort(0, len(DATA) - 1, len(DATA) - 1)

for el in DATA[::-1]:
    print(el[2])
