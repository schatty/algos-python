from random import randint

a = 1000
m = 123987123

for i0 in range(65, 123):
    print("i0", i0)
    for i1 in range(65, 123):
        for i2 in range(65, 123):
            for i3 in range(65, 123):
                for i4 in range(65, 123):
                    if i0 + i1 * a + i2 * a**2 + i3*a**3 + i4*a**4 % m == 0:
                        print("Found!")
                        break
