s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    syms_table = {}
    for i in range(len(s1)):
        sym1 = s1[i]
        sym2 = s2[i]

        if sym1 not in syms_table:
            if sym2 in syms_table.values():
                print("NO")
                break
            else:
                syms_table[sym1] = sym2
        elif syms_table[sym1] != sym2:
            print("NO")
            break
    else:
        print("YES")
