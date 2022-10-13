n, target = map(int, input().split())

weights = {}
tree = {}
for i in range(n):
    parent, w = map(int, input().split())

    if parent != -1:
        if parent not in tree:
            tree[parent] = [i]
        else:
            tree[parent].append(i)

    weights[i] = w

print("Tree", tree)
print("Weights", weights)

freq = {0: 1}

def count_paths(node_idx, prev_sum):
    cur_sum = prev_sum + weights[node_idx]

    res = 0
    if cur_sum - target in freq:
        print(cur_sum, " - ", target, " in " , freq)
        res += freq[cur_sum - target]

    if cur_sum not in freq:
        freq[cur_sum] = 1
    else:
        freq[cur_sum] += 1

    if node_idx in tree:
        for child in tree[node_idx]:
            res += count_paths(child, cur_sum)

    freq[cur_sum] -= 1

    return res


print(count_paths(0, 0))
