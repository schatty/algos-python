def calc_dist(a):
    dists = []

    cur = (-float("inf"), 0)
    for i, val in enumerate(a):
        if val > cur[0]:
            dists.append(i)
            cur = (val, i)
        else:
            dists.append(i - cur[1] - 1)

    print(dists)

    return max(dists)


a1 = [0, 1, 2, 0, 4]
print(calc_dist(a1))

a2 = [2, 3, 8, 5, 9, 1, 2, 3, 4, 5, 6]
print(calc_dist(a2))

