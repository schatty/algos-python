def max_dist(arr):
    queue = []
    dist = []

    for ind, val in enumerate(arr):
        while queue and val >= arr[queue[-1]]:
            queue.pop()

        queue.append(ind)
        if len(queue) == 1:
            dist.append(ind)
        else:
            diff = ind - queue[-2] - 1
            dist.append(diff)

    print(dist)
    return max(dist)

    

arr = [2,3,8,5,9,1,2,3,4,5,6]
res = max_dist(arr)
print(res)
