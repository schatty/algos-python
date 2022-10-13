M = int(input())
n = int(input())

stacks = []
for _ in range(n):
    c, kg = map(int, input().split())
    stacks.append([kg, c])

stacks.sort(key = lambda x: -x[1])
print("Stacks sorted:", stacks)

c_sum = 0
for kg, c in stacks:
    if M >= kg:
        M -= kg
        c_sum += kg * c
    else:
        c_sum += M * c
        break

print(c_sum)
    


