def compare():
    s1 = input().lower()
    s2 = input().lower()
   
    i1, i2 = 0, 0
    while i1 < len(s1) and i2 < len(s2):
        while i1 < len(s1) and (ord(s1[i1]) - 97 + 1) % 2 != 0:
            i1 += 1
        if i1 == len(s1):
            break

        while i2 < len(s2) and (ord(s2[i2]) - 97 + 1) % 2 != 0:
            i2 += 1
        if i2 == len(s2):
            break

        if s1[i1] != s2[i2]:
            if s1[i1] < s2[i2]:
                return -1
            else:
                return 1

        i1 += 1
        i2 += 1

    if i1 == len(s1) and i2 == len(s2):
        return 0

    if i1 == len(s1):
        while i2 != len(s2):
            if (ord(s2[i2]) - 97 + 1) % 2 == 0:
                return -1
            i2 += 1
        return 0

    if i2 == len(s2):
        while i1 != len(s1):
            if (ord(s1[i1]) - 97 + 1) % 2 == 0:
                return 1
            i1 += 1
        return 0

print(compare())
