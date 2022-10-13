def gen_matrix(n):
    def move(i, j, d, n):
        nonlocal direct
        
        new_level = False

        if direct == 0:
            if j == n - 1 - depth:
                i += 1
                direct = 1
            else:
                j += 1
        elif direct == 1:
            if i == n - 1 - depth:
                j -= 1
                direct = 2
            else:
                i += 1
        elif direct == 2:
            if j == 0 + depth:
                i -= 1
                direct = 3
            else:
                j -= 1
        else:
            if i == 1 + depth:
                new_level = True
                direct = 0
                j += 1
            else:
                i -= 1
 
        return i, j, new_level


    mm = [[0] * n for _ in range(n)]
    i, j = 0, 0
    cnt = 1
    depth = 0
    direct = 0
   
    while True:
        mm[i][j] = cnt

        if cnt == n * n:
            break

        (i, j, new_level) = move(i, j, depth, n)
        if new_level:
            depth += 1

        cnt += 1

    return mm


mm = gen_matrix(1)
for i in range(len(mm)):
    print(*mm[i])
