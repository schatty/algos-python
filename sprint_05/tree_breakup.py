class Node:  
    def __init__(self, left=None, right=None, value=0, size=0):  
        self.right = right
        self.left = left
        self.value = value
        self.size = size


def split(root, k):
    if root is None:
        return None, None

    # print("At root", root.value, k)

    # ->. We want all the nodes from the left subtree,
    # plus some nodes from the right
    if (root.left is None and k > 0) or (root.left and root.left.size + 1 <= k):
        # print("->")
        if root.left:
            k_fixed = k - (1 + root.left.size)
        else:
            k_fixed = k - 1
        left, right = split(root.right, k_fixed)
        # print("For node ", root.value, " left ", left, " right ", right, k)
        root.right = left
        
        # Update size
        if right:
            root.size -= right.size

        return root, right
   
    # print("<-")
    # <-. We want some nodes from the left tree
    left, right = split(root.left, k)
    # print("For node ", root.value, " left ", left, " right ", right, k)
    root.left = right

    if left is None and k >= 1:
        root_right = root.right
        if root.right:
            root.size -= root.right.size
            root.right = None
        return root, root_right

    if left:
        root.size -= left.size
    # print("Returning ", left, root)
    return left, root
    

def my_test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    print("Left size: ", left.size)
    assert(left.size == 4)
    assert(right.size == 2)


def my_test2():
    node1 = Node(None, None, 1, 1)
    node3 = Node(None, None, 3, 1)
    node2 = Node(node1, node3, 2, 3)

    node5 = Node(None, None, 5, 1)
    node7 = Node(None, None, 7, 1)
    node6 = Node(node5, node7, 6, 3)

    node9 = Node(None, None, 9, 1)
    node11 = Node(None, None, 11, 1)
    node10 = Node(node9, node11, 10, 3)

    node13 = Node(None, None, 13, 1)
    node15 = Node(None, None, 15, 1)
    node14 = Node(node13, node15, 14, 3)

    node12 = Node(node10, node14, 12, 7)
    node4 = Node(node2, node6, 4, 7)

    node8 = Node(node4, node12, 8, 15)

    left, right = split(node8, k=10)
    print("Test2 left size: ", left.size)
    assert left.size == 10
    assert right.size == 5


def my_test3():
    node1 = Node(None, None, 1, 1)
    node3 = Node(None, None, 3, 1)
    node2 = Node(node1, node3, 2, 3)

    l, r = split(node2, 0)
    print(l) #.value, l.size)
    print(r.value, r.size)

def my_test4():
    node = Node(None, None, 1, 1)
    l, r = split(node, 0)
    print(l)
    print(r, r.size)


def test1():
    node4 = Node(None, None, 266, 1)
    node3 = Node(None, node4, 191, 2)
    node2 = Node(node3, None, 298, 3)

    node10 = Node(None, None, 932, 1)
    node9 = Node(None, node10, 912, 2)
    node8 = Node(None, None, 822, 1)
    node7 = Node(node8, node9, 870, 4)
    node6 = Node(None, None, 701, 1)
    node5 = Node(node6, node7, 702, 6)

    node1 = Node(node2, node5, 668, 10)

    l, r = split(node1, 1)
    print(l.size, l.value)
    print(r.size, r.value)
    assert l.size == 1
    assert r.size == 9

def test2():
    node5 = Node(None, None, 130, 1)
    node7 = Node(None, None, 442, 1)
    node6 = Node(None, node7, 302, 2)
    node4 = Node(node5, node6, 220, 4)
    node9 = Node(None, None, 701, 1)
    node10 = Node(None, None, 858, 1)
    node8 = Node(node9, node10, 763, 3)
    node3 = Node(node4, node8, 545, 8)
    node2 = Node(None, node3, 31, 9)
    node1 = Node(node2, None, 867, 10)

    l, r = split(node1, 7)
    print(l.size, r.size)
    assert l.size == 7
    assert r.size == 3

# my_test()
# my_test2()
# my_test3()
# my_test4()

# test1()
# test2()
