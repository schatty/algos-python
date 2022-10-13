"""
https://contest.yandex.ru/contest/24414/run-report/69485134/

----------------------------- Idea ----------------------------

The implementation of a hash table via the "chaining" approach.
The underlying structure of the table is python list. The elements
of the list are either lists [KEY, VAL] or None in case of the 
empty content.

Implementation details:
    * During the `delete` operation we do not perform a shift for O(n)
      after the deletion. Instead, we put [None, None] for the deleted
      element. During `put` operation, we will check on previously 
      deleted elements.

------------------------ Time Complexity ----------------------

Initialization: O(n) as we need to allocate empty chains for each
of the n possible buckets.

GET - calculating the hash index = O(1); finding the corresponding key
      O(M), where M is the chain length. O(1) on average.
PUT - calculating the hash index = O(1); finding the empty spot for
      storing the element O(M), where M is the chain length. O(1) on
      average.
DELETE - calculating the hash index = O(1); finding the key = O(M), 
         shifting the chain after the deletion = O(M), 
         where M is the chain length. O(1) on average.

------------------------ Space Complexity ----------------------

O(N) for storing pointers to the lists (or None values)
O(N) for N elements itself.
Total: O(N)

"""
class HashTable:

    def __init__(self, size=100999, base=31):
        self.size = size
        self.p = base
        self.data = [[] for _ in range(size)]

    def get(self, key):
        ind = key % self.size
        l = self.data[ind]

        for k, v in l:
            if k == key:
                print(v)
                return
        else:
            print("None")

    def put(self, key, val):
        ind = key % self.size
        l = self.data[ind]

        for i, (k, v) in enumerate(l):
            if k == key:
                l[i] = [key, val]
                return
            elif k == key:
                l[i][1] = val
                return
        else:
            l.append([key, val])

    def delete(self, key):
        ind = key % self.size
        l = self.data[ind]

        for i, (k, v) in enumerate(l):
            if k == key:
                print(v)
                l.pop(i)
                return
        else:
            print("None")



table = HashTable()

n = int(input())
for _ in range(n):
    cmd, *args = input().split()
    if cmd == "get":
        table.get(int(args[0]))
    elif cmd == "put":
        table.put(int(args[0]), int(args[1]))
    else:
        table.delete(int(args[0]))
