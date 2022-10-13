def check_strings():
    s1 = input()
    s2 = input()

    l1, l2 = len(s1), len(s2)

    if abs(l2 - l2) > 1:
        print("FAIL")
        return

    n_mistakes = 0
    i1, i2 = 0, 0
    while i1 < l1 and i2 < l2:
        # print(s1[i1], s2[i2])
        if s1[i1] != s2[i2]:
            if n_mistakes == 1:
                print("FAIL")
                return

            # Skip symbol from the first string
            if i1 + 1 < l1 and s1[i1+1] == s2[i2]:
                i1 += 1
                n_mistakes += 1
            # Skip symbol from the second string
            elif i2 + 1 < l2 and s2[i2+1] == s1[i1]:
                i2 += 1
                n_mistakes += 1
            elif i1 + 1 < l1 and i2 + 1 < l2 and s1[i1 + 1] == s2[i2 + 1]:
                n_mistakes += 1
                i1 += 1
                i2 += 1
        else:
            i1 += 1
            i2 += 1

    # Check if we have some tails
    if l1 - i1 > 0 or l2 - i2 > 0:
        print("FAIL")
    else:
        print("OK")

check_strings()


