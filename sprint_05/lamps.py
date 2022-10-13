# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def recursive_search(node):
    if node is None:
        return -float("inf")

    if node.right is None and node.left is not None:
        return max(node.value, recursive_search(node.left))
    if node.right is not None and node.left is None:
        return max(node.value, recursive_search(node.right))
    if node.left is None and node.right is None:
        return node.value
    return max(node.value, recursive_search(node.left), recursive_search(node.right))


def solution(root):
    #  Your code
    #  “ヽ(´▽｀)ノ”
    sol = recursive_search(root)
    return sol


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


# test()
