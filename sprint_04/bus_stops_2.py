from math import sqrt


step = 20

def get_cell(x, y):
    if x < 0:
        cx = int(x // step) - 1
    else:
        cx = int(x // step)
    if y < 0:
        cy = int(y // step) - 1
    else:
        cy = int(y // step)
    return (cx, cy)

n = int(input())
metros = []
for i in range(n):
    x, y = input().split(" ")
    metros.append((int(x), int(y), i))

m = int(input())
bus_cells = {}
for _ in range(m):
    x, y = input().split(" ")
    cell =(int(x), int(y))
    bus_cells[cell] = bus_cells.get(cell, 0) + 1

print("bus_cells", bus_cells)

metro_max_ind = 0
metro_max_val = 0
for (x, y, ind) in metros:
    print("metro", x, y, ind)
    cells_seen = set()
    cur_metro_val = 0
    for dx in range(-20, 21):
        diff = int(sqrt(400 - dx * dx))
        for dy in range(-diff, diff+1):
            bus_cell = ((x - dx), (y + dy))
            if bus_cell in cells_seen:
                continue
            cells_seen.add(bus_cell)

            cur_metro_val += bus_cells.get(bus_cell, 0)

    if cur_metro_val > metro_max_val or (cur_metro_val == metro_max_val and metro_max_ind > ind):
        print("Updating the metro")
        metro_max_val = cur_metro_val
        metro_max_ind = ind


print(metro_max_ind + 1)


 
