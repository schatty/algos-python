n = int(input())
nums = list(map(int, input().split()))
k = int(input())

diffs = []
for i in range(n - 1):
    for j in range(i+1, n):
        print(i, j)
        diff = abs(nums[i] - nums[j])

        if len(diffs) == k:
            i_max = 0
            max_el = diffs[0]
            for z in range(1, len(diffs)):
                if diffs[z] > max_el:
                    max_el = diffs[z]
                    i_max = z
            print("diffs: ", diffs)
            print("diff max_el", diff, max_el)
            print()
            if diff < max_el:
                diffs[i_max] = diff

        else:
            diffs.append(diff)

diffs.sort()
print(diffs)
print(diffs[k - 1])
