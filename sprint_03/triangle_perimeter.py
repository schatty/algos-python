n = int(input())
sides = list(map(int, input().split()))

sides.sort()

i = len(sides) - 1
while i > 2:
    if sides[i] < sides[i - 1] + sides[i - 2]:
        break
    i -= 1

print(sides[i] + sides[i - 1] + sides[i - 2])
