# Comment it before submitting
# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left


def calc_height(node):
    if node is None:
        return 0
    return max(calc_height(node.left), calc_height(node.right)) + 1


def solution(root):
    if root is None:
        return True

    l_height = calc_height(root.left)
    r_right = calc_height(root.right)
    if abs(l_height - r_right) <= 1 and solution(root.left) and solution(root.right):
        return True
    return False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


# test()
