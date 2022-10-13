n = int(input())
seq1 = []
for _ in range(n):
    x, y = map(int, input().split())
    seq1.append([x, y])

seq2 = []
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    seq2.append([x, y])

def get_instesec():
    if m == 0 or n == 0:
        return

    i1 = 0
    i2 = 0
    intersec = []
    while i1 < len(seq1) and i2 < len(seq2):
        if seq1[i1][0] > seq2[i2][0]:
            if seq1[i1][0] > seq2[i2][1]:
                i2 += 1
                continue
            start = seq1[i1][0]
            seq2[i2][0] = seq1[i1][0]
        else:
            if seq2[i2][0] > seq1[i1][1]:
                i1 += 1
                continue
            start = seq2[i2][0]
            seq1[i1][0] = seq2[i2][0]

        if seq1[i1][1] < seq2[i2][1]:
            end = seq1[i1][1]
            i1 += 1
        else:
            end = seq2[i2][1]
            i2 += 1

        intersec.append([start, end])

    for inter in intersec:
        print(*inter)


get_instesec()
