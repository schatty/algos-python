s_sub = input()
s_source = input()

sym_ind = 0
sym = s_sub[sym_ind]

for s in s_source:
    if s == sym:
        sym_ind += 1
        if sym_ind == len(s_sub):
            break
        sym = s_sub[sym_ind] 

print(sym_ind == len(s_sub))

    
