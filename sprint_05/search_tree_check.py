# Comment it before submitting
# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left

def recursive_check(node, parent_node=None):
    if node is None:
        return True

    # Check children

    if node.left is not None:
        if node.left.value >= node.value:
            return False
    
    if node.right is not None:
        if node.right.value <= node.value:
            return False

    # Check parent's limit

    if parent_node is not None:
        if node is parent_node.left:
            if node.right and node.right.value >= parent_node.value:
                return False
        else:
            if node.left and node.left.value <= parent_node.value:
                return False

    # Recursive call

    if node.left is not None and not recursive_check(node.left, node):
        return False

    if node.right is not None and not recursive_check(node.right, node):
        return False

    return True


def solution(root) -> bool:
    return recursive_check(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


# test()
