'''
https://contest.yandex.ru/contest/22781/run-report/69007779/

Calculator via the polyak notation.

----------------------------- Idea ----------------------------

The stack data structure is at the core of the algorithm.
The procedure:
    1. If read symbol is an opertation, pop two last elements from
       the stack and perform the operation on them. Then push the result
       at the top of the stack.
    2. If read symbol is a number, add this number at the top of
       the stack.
    3. If no symbols left, output the single left elment on the stack.

------------------------ Time Complexity ----------------------

O(n), where n is the size of given symbol sequence. For each of the 
sybmol from a sequence we need either performing operation or storing 
the.

------------------------ Space Complexity ----------------------

O(n). The worst case scenario is when we first receive only
numbers, then only operators. In this case we will store n / 2 
numbers (as the rest n/2 will be operators to dissolve stored
numbers). For the best case of the "paired"
    number -> operator -> number -> ...
sequence we only need to store 2 numbers on a stack.

'''

expr = input().split(" ")

ops = {
        "*": lambda a, b: a * b,
        "/": lambda a, b: b // a,
        "+": lambda a, b: a + b,
        "-": lambda a, b: b - a
}
stack = []
for s in expr:
    op = ops.get(s)
    if op is None:
        stack.append(int(s))
    else:
        a, b = stack.pop(), stack.pop()
        stack.append(op(a, b))
print(stack.pop())
