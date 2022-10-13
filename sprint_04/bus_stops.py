d_step = 20 # 1415

n = int(input())
metros = {}
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)

    metro_cell = (int(y // d_step), int(x // d_step))
    if metro_cell not in metros:
        metros[metro_cell] = [(x, y, i)]
    else:
        metros[metro_cell].append((x, y, i))

# print("Metros", metros)

m = int(input())
buses = []
metros_cnt = {}
metros_cnt_max = 0
metros_cnt_order = float("inf")
for _ in range(m):
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)

    cy, cx = int(y2 // d_step), int(x2 // d_step)
    bus_cells = [(cy, cx), (cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1), (cy - 1, cx - 1), (cy - 1, cx + 1), (cy + 1, cx - 1), (cy + 1, cx + 1)]
    for bus_cell in bus_cells:
        metro_cell = metros.get(bus_cell)
        if metro_cell is not None:
            for metro in metro_cell:
                x1, y1, order = metro
                if (x1 - x2)**2 + (y1 - y2)**2 <= 400:
                    if (x1, y1) not in metros_cnt:
                        metros_cnt[(x1, y1)] = 1
                    else:
                        metros_cnt[(x1, y1)] += 1

                    metro_val = metros_cnt[(x1, y1)]
                    if metro_val > metros_cnt_max:
                        metros_cnt_max = metro_val
                        metros_cnt_order = order
                    elif metro_val == metros_cnt_max:
                        if  order < metros_cnt_order:
                            metros_cnt_max = metro_val
                            metros_cnt_order = order
                    

print(metros_cnt_order + 1)
