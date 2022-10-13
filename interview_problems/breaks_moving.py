"""
You have a heaps of `n` stones. i-th heap weights `a_i` kg. Heaps
can be merged with each other, in that case a_i + a_j energy points
is used, two original heaps disappear and the new one of weight a_i + a_j
appears. Calculate the least amount of energy required to combine all the
stones.

Idea:
    * Notice that the least amount of energy is spent when we merge two
    heaps with the least weights. 
    * We sort the original array in reverse order and then work with it
      as a tack putting the newly emerged heap on top. Then we merge
      two heaps on top. We sum the spent energy in the variable.

"""

n = int(input())
a = list(map(int, input().split()))


a.sort(reverse=True)

def get_energy():
    if n == 1:
        return a[0]

    energy = 0
    while len(a):
        a_i = a.pop()
        if len(a) == 0:
            break

        a_j = a.pop()
        a.append(a_i + a_j)
        energy += a_i + a_j

    return energy

print(get_energy())

