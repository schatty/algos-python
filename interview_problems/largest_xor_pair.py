class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


def largest_xor(a):
    root = TrieNode()

    for n in a:
        n_str = bin(n)[2:].zfill(32)
        node = root
        for b in n_str:
            if b not in node.children:
                node.children[b] = TrieNode()
            node = node.children[b]
        else:
            node.terminal = True

    max_xor = 0

    for n in a:
        opposite = ''
        n_str = bin(n)[2:].zfill(32)
        node = root
        for b in n_str:
            if b == '0':
                op = '1'
            else:
                op = '0'

            if op in node.children:
                opposite += op
                node = node.children[op]
            else:
                opposite += b
                node = node.children[b]

        xor = int(''.join(opposite), 2) ^ n
        max_xor = max(max_xor, xor)

    return max_xor


print(largest_xor([1, 8, 3, 1, 4]))
print(largest_xor([4, 8, 1024]))
print(largest_xor([10, 10]))
