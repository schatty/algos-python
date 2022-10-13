from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbours = []


    
def cloneGraph(node) -> Node:

    seen = {}

    def dfs(node, seen):
        new_node = Node(node.val)
        seen[node.val] = new_node

        new_neighbors = []
        for nb in node.neighbours:
            if nb in seen:
                new_neighbors.append(seen[nb.val])
            else:
                new_neighbors.append(dfs(nb, seen))

        new_node.neighbours = new_neighbors

        return new_node

    return dfs(node, seen)


def print_graph(start_node):
    node_stack = [start_node]

    while len(node_stack):
        node = node_stack.pop()
        print("Node", node.val)
        for neighbor in node.neighbours:
           node_stack.append(neighbor)


def test():
    node5 = Node(5)
    node6 = Node(6)
    
    node2 = Node(2)
    node2.neighbours = [node5, node6]

    node7 = Node(7)
    node4 = Node(4)
    node4.neighbours = [node7]

    node3 = Node(3)
    node1 = Node(1)
    node1.neighbours = [node2, node3, node4]

    print_graph(node1)
    print()

    node1_clone = cloneGraph(node1)
    print_graph(node1_clone)

# test()
