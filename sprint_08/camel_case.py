class Node:
    def __init__(self, sym):
        self.sym = sym
        self.words = []
        self.neighbors = {}

    def __str__(self):
        s = f"Node {self.sym}: {[w for w in self.words]} {self.neighbors}"
        if len(self.neighbors):
            for k, v in self.neighbors.items():
                s += "\n" + str(v)
        return s



def camel_case():
    n = int(input())
    trie = Node("")
    for _ in range(n):
        w = input()
        path = [s for s in w if s.isupper()]
        # print("Word", w, path)

        node = trie
        for i, sym in enumerate(path):
            if sym not in node.neighbors:
                node.neighbors[sym] = Node(sym)
            # print("Now node is", node)
            node = node.neighbors[sym]
        node.words.append(w)

    # print("Trie", trie)


    def collect_words(node, query, words):
        # print("Collecting for ", node.sym, query, words)
        if len(query) == 0:
            for w in node.words:
                words.append(w)
            for n in node.neighbors.values():
                collect_words(n, query, words)

            return

        if query[0] not in node.neighbors.keys():
            words.clear()
            return

        collect_words(node.neighbors[query[0]], query[1:], words)


    m = int(input())
    for _ in range(m):
        query = input()
        words = []
        collect_words(trie, query, words)
        for w in sorted(words):
            print(w)
 

camel_case()
