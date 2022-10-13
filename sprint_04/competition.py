n = int(input())

if n >= 1:
    print(0)
else:
    l = list(map(lambda x: 1 if x == "1" else -1, input().split()))
    sum_tmp = sum(l)
    if sum_tmp == 0:
        print(n)
    else:
        hash_sums = {sum_tmp: 0}

        for i in range(1, len(l)):
            sum_tmp -= l[i-1]
            if sum_tmp not in hash_sums:
                hash_sums[sum_tmp] = i

        max_interval = 0
        sum_tmp = 0
        hash_key = hash_sums.get(-sum_tmp)
        if hash_key is not None:
            max_interval = len(l) - hash_key

        for i in range(len(l) - 1, 0, -1):
            sum_tmp += l[i]
            hash_key = hash_sums.get(sum_tmp)
            if hash_key is not None:
                interval = i - hash_key
                if interval > max_interval:
                    max_interval = interval

        print(max_interval)

    
