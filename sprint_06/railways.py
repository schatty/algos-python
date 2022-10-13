"""
https://contest.yandex.ru/contest/25070/run-report/69696462/

----------------------------- Idea ----------------------------

We combine two undirectional road types into one directional graph.
The R-roads connects i-th with to j-th (i < j), and B-roads connects
j-th roads to i-th (i < j). This way if it's possible to travel between
any two nodes with in two different directions, we will have a cycle.

Base case: a graph has only 3 nodes. Assume that a cycle exists, then we 
have paths 1→2, 2→3, 3→1. In the original graph roads 1→2, 2→3 have type R,
and road 3→1 has type B which means we can travel from 1 to 3 using roads
of two types. Therefore the graph is not optimal.

Transition: let’s assume that every graph of size k that doesn’t have cycles
if the graph is optimal.

k+1 case: We remove the k+1 node and sort the graph topologically, let p_i 
be the node that has i-th place in a topological sort. We bring back k+1
node. Assume that now we have a cycle. Nodes p_{0…i} leads to the k+1 node
and k+1 leads to nodes p_{i+1,…k}. Then there exist such nodes p_{i}, 
p_{i+1} s.t. we have path from p_{i+1} to k+1 and from k+1 to i which means 
the graph is not optimal.

------------------------ Time Complexity ----------------------

* Graph construction, worst case is we have V * (V+1) / 2 = O(V^2)
  edges

* DFS worst case: there will be no cycle and each i-th node is connected
  to all the further j=i+1..N nodes with the same direction. In this case 
  for every node V we will walk to all of the j-th nodes i.e. O(V^2)

T = O(V^2) + O(V^2)

------------------------ Space Complexity ----------------------

* Worst case, we need V * (V+1) / 2 variables for edges for each of
the roads type i.e. O(V^2)

T = O(V^2)

"""

def dfs_cycle(g) -> bool:
    n = len(g)     # Including the last node without oucoming edges (+1)
    color = [0] * n
    stack = [0]
    visited = 1
    v = None

    while len(stack) or visited < n:
        # If the sack is empty, find other disconnected component
        if len(stack) == 0:
            for i in range(n):
                if color[i] == 0:
                    stack.append(i)
                    break

        v = stack.pop()
        if color[v] == 0:
            visited += 1

            # Node is gray now, add to the to-be visited
            color[v] = 1
            stack.append(v)

            if len(g[v]) > 0:
                for v_out in g[v]:
                    if color[v_out] == 0:
                        stack.append(v_out)
                    # Cycle condition - we come to the node that has
                    # been already reached from other node
                    elif color[v_out] == 1:
                        return True

        elif color[v] == 1:
            color[v] = 2

    return False


# Number of nodes
n = int(input())

g = [[] for _ in range(n)]
# Starting node don't include the last one
for i in range(n - 1):
    # Outcoming nodes don't include the i-th node
    for j, s in enumerate(input(), start=i + 1):
        if s == "R":
            g[i].append(j)
        else:
            g[j].append(i)


cycle_exist = dfs_cycle(g)
if cycle_exist:
    print("NO")
else:
    print("YES")

