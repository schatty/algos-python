"""
https://contest.yandex.ru/contest/26133/run-report/70257451/

----------------------------- Idea ----------------------------

We use single dynamic programming array of size of the text with i-th 
element equal to 1 if the corresponding symbol is the terminal one.
Our answer is the last element in DP, if it's 1, then the string can
be split into existing words.

How to determine if the symbol is terminal? We build the trie from
the set of given words and consider the leaves as terminal symbols.

How to fill DP array? We will loop over 0..len(S) in dynamic array,
and start checking all the subsequent characters from the nearest
DP[i] == 1. Starting from index i, we loop over all the remaining
characters finding terminal states in the trie.

Implementation details:
    * A trie is using arrays with i-th index corresponding to the i-th
      symbol in English alphabet.
    * We append one more symbol to represent a termninal state.

------------------------ Time Complexity ----------------------

* We need to check every i-th symbol from the original string as
  a possible starting point: O(n)
* For each of the symbol we need to run remaining characters through
  the trie for finding terminal states. As we use array with constant
  indexing time in the trie, the average complexity would also be O(n)

Total: O(N^2)

------------------------ Space Complexity ----------------------

* We need N symbols for the DP array.
* For building trie with arrays we would need at least N * 27 space for
  arrays for each of the N-th symbol.

Total: O(N)

"""

class TrieNode:
    def __init__(self):
        self.paths = [None] * 26
        self.terminal = False

    def path_exists(self, ind):
        return self.paths[ind]

    def get_path(self, ind):
        return self.paths[ind]

    def add_path(self, ind):
        self.paths[ind] = TrieNode()


def build_trie(words):
    trie = TrieNode()

    for word in words:
        node = trie
        for s in word:
            idx = ord(s) - 97
            if not node.path_exists(idx):
                node.add_path(idx)

            node = node.get_path(idx)
        else:
            node.terminal = True

    return trie


def check_sentence(trie, s):
    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for i in range(len(s) + 1):
        node = trie
        
        # Loop starts only from 1-th
        if dp[i] == 0:
            continue

        # + 1 as we have 'termnial' leaf that doesn't have the corresponding symbol in text
        for j in range(i, len(s) + 1):
            if node.terminal:
                dp[j] = 1

            if j == len(s):
                break

            idx = ord(s[j]) - 97
            if not node.path_exists(idx):
                break
            
            node = node.get_path(idx)

    return dp[-1]


s = input()
n = int(input())
words = (input() for _ in range(n))

trie = build_trie(words)
if check_sentence(trie, s):
    print("YES")
else:
    print("NO")
