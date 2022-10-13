# Comment it before submitting
# class Node:  
#     def __init__(self, left=None, right=None, value=0):  
#         self.right = right
#         self.left = left
#         self.value = value


def print_range(node, l, r):
    if node is None:
        return None

    if node.value < l:
        print_range(node.right, l, r)
    
    else:
        # node.value >= l
        print_range(node.left, l, r)
        if node.value <= r:
            print(node.value)
            print_range(node.right, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

# test()
