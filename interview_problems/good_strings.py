"""
The string is called "good" if it doesn't contain two adjacent symbols of different
cases. The string can be modified: two adjacent symbols in different cases can
be deteled. Thus every string can be modified to be "good" via the sequence of
such modifications. Given the string, return its "good" form.

Solution:
    * We will use stack and iteratively append 1..N symbol on top of it. After
      new symbol is added, we check is the latest symbols can be removed.
"""


s = input()

def reduce_string(s):
    n = len(s)
    if n == 1:
        return s

    stack = []
    for sym in s:
        stack.append(sym)

        if len(stack) > 1 and stack[-1].lower() == stack[-2].lower():
            if stack[-1].islower() and stack[-2].isupper() or stack[-1].isupper() and stack[-2].islower():
                stack.pop()
                stack.pop()

    return ''.join(stack)

print(reduce_string(s))
