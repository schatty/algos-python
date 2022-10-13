"""
https://contest.yandex.ru/contest/25070/run-report/69640168/

----------------------------- Idea ----------------------------

* Use Prim algorithm for finding minimal spanning tree.
* Replace min operation with max for finding maximum spanning treee.
* Use heap data structure for stroring tacking edges - the edge with
  maximum weight will be on the top -> takes O(1) for popping and O(log|V|)
  for adding.

------------------------ Time Complexity ----------------------

* Storing graph: O(|E|) as we need to store each edge.
* Prime algorithm with heap: O(|E| * log|E|)

T = O(|E| * log|E|)

------------------------ Space Complexity ----------------------

* Worst case: the graph is fully connected i.e. O(V^2)

"""

from heapq import heappush, heappop


n, m = map(int, input().split())

g = [{} for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    
    # Skip self-connected nodes
    if u == v:
        continue

    if v not in g[u]:
        g[u][v] = w
    else:
        # Updating edge only if new weight is bigger
        if (g[u][v] < w):
            g[u][v] = w

    if u not in g[v]:
        g[v][u] = w
    else:
        if (g[v][u] < w):
            g[v][u] = w


def extract_minimum(edges):
    w, out = heappop(edges)
    return out, -w


def add_vertex(g, not_added, edges, v) -> None:
    """Tracks newly added vertex to the span-tree and
    modifies existing edges to consider. 

    vertex `v` is guaranteed to be in graph `g`.
    """
    not_added.remove(v)
    for out, w in g[v].items():
        if w and out in not_added:
            # Storing negative weight as working with min-heap
            heappush(edges, (-w, out))


def calc_max_span_tree(g):
    """Calculate the weight of the max spanning tree.
    Returns int if tree is found and None is the graph is
    disconnected.
    """
    max_span_tree = 0
    not_added = set(range(n))
    edges = []
    v = 0

    # Edge cases
    if len(not_added) == 1:
        return 0
    # if v not in g:
    if len(g) == 0:
        return None

    # Startin vertex
    add_vertex(g, not_added, edges, v)

    while len(not_added) and len(edges):
        v, w = extract_minimum(edges)
        if v in not_added:
            max_span_tree += w
            add_vertex(g, not_added, edges, v)

    # If some node reamin unreached, then the graph is disconnected
    if len(not_added):
        return None
    return max_span_tree


span_tree_weight = calc_max_span_tree(g)
if span_tree_weight is None:
    print("Oops! I did it again")
else:
    print(span_tree_weight)
