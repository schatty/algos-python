from typing import List, Optional


class Node:
    def __init__(self) -> None:
        self.id = None
        self.left = None
        self.right = None


def get_tree_border(root: Node) -> List[int]:
    borders = set()

    def boundary_left(node):
        nonlocal borders
        
        if node:
            if node.left:
                borders.add(node.id)
                boundary_left(node.left)
            elif node.right:
                borders.add(node.id)
                boundary_left(node.right)

    def boundary_right(node):
        nonlocal borders

        if node:
            if node.right:
                boundary_right(node.right)
                borders.add(node.id)
            elif node.left:
                boundary_right(node.left)
                borders.add(node.id)

    def leaves(node):
        nonlocal borders

        if node:
            leaves(node.left)

            if node.left is None and node.right is None:
                borders.add(node.id)

            leaves(node.right)

    boundary_left(root)
    boundary_right(root)
    leaves(root)

    return list(borders)

def read_tree() -> Node:
    size, root_id = map(int, input().split())
    nodes = [Node() for i in range(size)]
    for i in range(size):
        left, right = map(int, input().split())
        nodes[i].id = i
        nodes[i].left = nodes[left] if left != -1 else None
        nodes[i].right = nodes[right] if right != -1 else None
    return nodes[root_id]


tree = read_tree()

print(*get_tree_border(tree))
