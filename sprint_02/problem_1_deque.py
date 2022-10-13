'''
https://contest.yandex.ru/contest/22781/run-report/69007675/

Deque with all operations with O(1)

----------------------------- Idea ----------------------------

The deque data structure is implemented using a single array of
given length. We will use two pointers as `head` and `tail`:
    `head` - points to the "start" of the stored sequence,
             adding an element to the head means expanding
             current boundary leftwards.
    `tail` - points to the "end" of the stored sequence,
             adding an element to the tail means expanding
             current boundary rightwards.

Implementations details:
    `head` - points to the next empty cell of an array.
    `tail` - points to the cell containing the last element.

------------------------ Time Complexity ----------------------

First operation: initializaton of a data structure, takes O(1)

Adding an element to the tail: Assign array cell, move tail pointer ->: O(1)
Removing an element from the tail: move tail pointer <-, read array cell: O(1)
Adding an element to the head: Move head pointer <-, assign array cell: O(1)
Removing an element from the head: Read array cell, move head pointer ->: O(1)

------------------------ Space Complexity ----------------------

Wee need an array of size `m` for storing all the data. The
pointers for the head and the tail are two additional variables.
The final space complexity: O(m)

'''

class Deque:
    def __init__(self, m):
        self.deque = [0] * m
        self.head = 0
        self.tail = 0
        self.cur_size = 0
        self.capacity = m

    def push_back(self, x: int):
        if self.cur_size == self.capacity:
            print("error")
            return
        self.deque[self.tail] = x
        self.tail = (self.tail + 1) % m
        self.cur_size += 1

    def pop_front(self):
        if self.cur_size == 0:
            print("error")
            return
        x = self.deque[self.head]
        self.deque[self.head] = 0
        self.head = (self.head + 1) % m
        self.cur_size -= 1
        print(x)

    def pop_back(self):
        if self.cur_size == 0:
            print("error")
            return
        ind = (self.tail - 1) % m
        x = self.deque[ind]
        self.tail = ind
        self.cur_size -= 1
        print(x)

    def push_front(self, x: int):
        if self.cur_size == m:
            print("error")
            return
        ind = (self.head - 1) % m
        self.deque[ind] = x
        self.head = ind
        self.cur_size += 1


n = int(input())  # Number of commands
m = int(input())  # Size of the deque

deque = Deque(m)

for _ in range(n):
    cmd, *vals = input().split()
    if cmd == "push_back":
        deque.push_back(int(vals[0]))
    elif cmd == "pop_front":
        deque.pop_front()
    elif cmd == "pop_back":
        deque.pop_back()
    elif cmd.startswith("push_front"):
        deque.push_front(int(vals[0]))

