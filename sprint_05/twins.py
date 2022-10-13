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

    
def solution(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    l_nodes = []
    lmr_walk(root1, l_nodes)
    r_nodes = []
    lmr_walk(root2, r_nodes)

    if len(l_nodes) != len(r_nodes):
        return False

    for i in range(len(l_nodes)):
        if l_nodes[i] != r_nodes[i]:
            return False
    return True


def test():
    node1 = Node(1,  None,  None)
    node2 = Node(2,  None,  None)
    node3 = Node(3,  node1,  node2)

    node4 = Node(1, None,  None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)
    
    assert solution(node3, node6)

# test()
