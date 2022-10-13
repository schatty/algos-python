"""
https://contest.yandex.ru/contest/24810/run-report/69553582/

----------------------------- Idea ----------------------------

The function `remove` will accomplish the following
    
    I. Recursively find the element with given key in a tree.
    II. Remove the element from the tree. Three cases are considered:
        (0). Found node is Node, do nothing
        (1). Found node has not children, just delete it then.
        (2). Found node has only one children - the children takes
             place of the deleted node
        (3). Found node has two children. 
                - find min element from the right children branch
                - assign min-element value to the deleted node's value
                - Recursively run (II) on the right branch of the 
                  deleted node.

------------------------ Time Complexity ----------------------

* O(log n) - finding element
* O(log n) - recursive deletion of the node in the worst case.

T = O(log n) + O(log n) = O(log n)

------------------------ Space Complexity ----------------------

The deletion operation doesn't require additional memory (except 
the rerusive stack trace) as it modifies only existing tree structure.

T = O(1)

"""


class Node:  
    def __init__(self, left=None, right=None, value=0):  
        self.right = right
        self.left = left
        self.value = value


def find_leftmost(node):
    parent = None
    cur = node
    while cur.left:
        parent = cur
        cur = cur.left
    return cur, parent


def remove(root, key):
    d = root
    d_parent = None
    while d and d.value != key:
        d_parent = d
        if key < d.value:
            d = d.left
        elif key > d.value:
            d = d.right

    # Check if key was found?
    if d is None:
        return None

    # Case #1. Tree consists only from one node
    # if d.left is None and d.right is None:
    #     root = None
    #     break

    # Case #1, #2. Node has only one child
    if d.left is None or d.right is None:
        new_node = None

        if d.left is None:
            new_node = d.right
        else:
            new_node = d.left

        if d_parent is None:
            return new_node

        if d is d_parent.left:
            d_parent.left = new_node
        else:
            d_parent.right = new_node
    
    # Case #3. Node has two child
    # We replace the value of the node and run it recursively
    else:
        p, p_parent = find_leftmost(d.right)

        # leftmost element is the child of the deleted node
        if p_parent is None:
            d.right = p.right
        # leftmost parent has parent which shouldn't left childless
        else:
            p_parent.left = p.right

        d.value = p.value

    return root

def get_size(node):
    if node is None:
        return 0
    return get_size(node.left) + get_size(node.right) + 1

def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
    assert newHead.right.left is node4
    # print("Success")

def test2():
    node10 = Node(None, None, 932)
    node9 = Node(None, node10, 912)
    node8 = Node(None, None, 822)
    node6 = Node(node8, node9, 870)
    node5 = Node(None, None, 701)
    node7 = Node(None, None, 266)
    node4 = Node(None, node7, 191)
    node3 = Node(node5, node6, 702)
    node2 = Node(node4, None, 298)
    node1 = Node(node2, node3, 668)

    newHead = remove(node1, 702)
    newHead = remove(node1, 266)
    newHead = remove(node1, 822)
    print(newHead.right.value)
    assert newHead.right.value ==  870

    print(newHead.left.value, newHead.right.value)
    print(newHead.left.left.value, newHead.right.left.value)
    print(newHead.right.right.value)
    print(newHead.right.right.right.value)
    print(newHead.left.right)

    print(get_size(newHead))

# test()
# test2()
