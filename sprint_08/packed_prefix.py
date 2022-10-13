"""
https://contest.yandex.ru/contest/26133/run-report/70235806/

----------------------------- Idea ----------------------------

We solve the problem in 2 steps:
    1. Unpack the current string recursively
    2. Update the current prefix as a common prefix of the current string
       and a previous prefix.

------------------------ Time Complexity ----------------------

N - number of given strings
M - max length of given strings

* Unpacking string: we should process each of the given symbols, worst case
  - O(M)
* Comparing the prefixes: we should process each of the symbols from 
  two given strings: O(M)

Total: O(M * N)

------------------------ Space Complexity ----------------------

We need to store two strings: one for the current common prefix
(the size of the prefix wil be decreasing and can be M as maximum),
and other for the current string from the stream (O(M) at max).

Total: O(M)

"""

def get_common_prefix_index(s1: str, s2: str) -> int:
    m = min(len(s1), len(s2))
    for i in range(m):
        if s1[i] != s2[i]:
            return i
    return m


def unpack(s: str) -> str:
    """Unpacks multiplicative components. """

    s_unpacked = ""
    i = 0
    i_slow = 0
    while i < len(s):
        if s[i].isdigit():
            if i_slow < i:
                s_unpacked += s[i_slow:i]
            mul = int(s[i])
            i += 2  # skipping [N
            i_start = i
            brackets_closed = 1
            while i < len(s):
                if s[i] == '[':
                    brackets_closed += 1
                elif s[i] == ']':
                    brackets_closed -= 1
                if brackets_closed == 0:
                    break
                i += 1

            s_unpacked += mul * unpack(s[i_start:i])
            i += 1 # skipping ]
            i_slow = i
        else:
            i += 1

    if i_slow < i:
        s_unpacked += s[i_slow:i]

    return s_unpacked

def get_prefix():
    n = int(input())

    prefix = unpack(input())
    for _ in range(1, n):
        s = unpack(input())
        ind = get_common_prefix_index(s, prefix)
        if ind == 0:
            return ""
        prefix = prefix[:ind]

    return prefix

print(get_prefix())
