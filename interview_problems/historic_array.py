n = int(input())
q = int(input())

hsh = [{0: 0} for _ in range(n)]
cur_era_id = 0
for _ in range(q):
    cmd, *args = input().split()
    if cmd == "set":
        idx, value = map(int, args)
        hsh[idx][cur_era_id] = value
    
    elif cmd == "begin_new_era":
        cur_era_id = int(args[0])
    else:
        idx, era_id = map(int, args)
        for era, val in hsh[idx].items():
            if era == era_id:
                print(val)
                break
