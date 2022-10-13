n = int(input())
beds = []
for _ in range(n):
    x, y = map(int, input().split())
    beds.append((x, y)) 

beds.sort(key=lambda x: x[0])

beds_merged = [beds.pop(0)]
for bed in beds:
    # Case #1 - appeneded bed is part of the last bed
    if bed[0] >= beds_merged[-1][0] and bed[1] <= beds_merged[-1][1]:
        pass

    # Case #2 - appended bed expands last bed
    elif bed[0] <= beds_merged[-1][1] and bed[1] > beds_merged[-1][1]:
        new_x = beds_merged.pop()[0]
        beds_merged.append((new_x, bed[1]))

    # Case #3 - non overlapping bad
    else:
        beds_merged.append(bed)


for bed in beds_merged:
    print(*bed)
