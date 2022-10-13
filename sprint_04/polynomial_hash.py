a = int(input())
m = int(input())
st = input()

n = len(st)
h = 0
for s in st:
    h = (h * a + ord(s)) % m

print(h)
