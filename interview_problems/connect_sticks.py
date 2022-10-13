n = int(input())
a = list(map(int, input().split()))

import heapq

heapq.heapify(a)

res = 0

while len(a) > 1:
    first = heapq.heappop(a)
    sec = heapq.heappop(a)
    res += first + sec
    heapq.heappush(a, first + sec)

print(res)
