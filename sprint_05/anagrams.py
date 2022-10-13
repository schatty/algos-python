# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def lmr_walk(node, a):
    if node is None:
        return

    lmr_walk(node.left, a)
    a.append(node.value)
    lmr_walk(node.right, a)


def solution(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return False
    if root.right is None:
        return False

    nodes_l = []
    lmr_walk(root.left, nodes_l)
    nodes_r = []
    lmr_walk(root.right, nodes_r)

    if len(nodes_l) != len(nodes_r):
        return False

    for i in range(len(nodes_l)):
        if nodes_l[i] != nodes_r[-i-1]:
            return False

    return True


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


test()
