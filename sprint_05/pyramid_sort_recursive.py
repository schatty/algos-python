"""
https://contest.yandex.ru/contest/24810/run-report/69544150/

----------------------------- Idea ----------------------------

Sorting algorithm with min-heap.
Approach:
    * Store every N element in the min-heap structure.
    * Retrieve the root of the min-heap N times, obtaining 
      the most minimal element from the heap each time.

------------------------ Time Complexity ----------------------

* O(1) - Allocating min-heap
* Adding every element to the min-heap has an upper bound of O(n * log n * m),
  where m is the average length of a string invlolving in sorting.
* Retrieving every element from the min-heap has upper bound of O(n * log n * m)

T = O(1) + O(n log n * m) + O(n log n * m) = O(n * log n * m)

------------------------ Space Complexity ----------------------

* O(N) for storing the heap in the array.
* O(N) for the storing N elements in sorted order.

T = O(N) + O(N) = O(N)

"""

n = int(input())

def sift_up(heap, idx):
    if idx == 1:
        return 1

    parent_idx = idx // 2
    # Below we use ">=" but it's < for original data
    if heap[parent_idx] >= heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        return sift_up(heap, parent_idx)

    return idx


def heap_add(heap, key):
    idx = len(heap)
    heap.append(key)
    sift_up(heap, idx)


def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1

    if len(heap) - 1 < left:
        return idx

    # Below we use ">=" but it's "<" for the original data
    if right <= len(heap) - 1 and heap[left] >= heap[right]:
        idx_largest = right
    else:
        idx_largest = left

    if heap[idx] >= heap[idx_largest]:
        heap[idx], heap[idx_largest]= heap[idx_largest], heap[idx]
        return sift_down(heap, idx_largest)
    return idx


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]

    heap.pop(len(heap) - 1)
    sift_down(heap, 1)    

    return result

# 0th element should exist
heap = [-1]

# Reading data and adding it to the heap
for _ in range(n):
    login, points, penalty = input().split()
    item = (-int(points), int(penalty), login)
    heap_add(heap, item)

# Retreave min elements from the heap
for _ in range(n):
    item = pop_max(heap)
    print(item[2])

    
