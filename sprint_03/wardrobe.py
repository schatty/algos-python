n = int(input())
seq = input().split()

cnt = [0] * 3
for s in seq:
    if s == '0':
        cnt[0] += 1
    elif s == '1':
        cnt[1] += 1
    else:
        cnt[2] += 1

if cnt[2] > 1:
    print('0 ' * cnt[0] + '1 ' * cnt[1] + '2 ' * (cnt[2] - 1) + '2')
elif cnt[2] == 1:
    print('0 ' * cnt[0] + '1 ' * cnt[1] + '2 ')
else:
    print('0 ' * cnt[0] + '1 ' * cnt[1])
