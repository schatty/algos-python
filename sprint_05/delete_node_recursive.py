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
    cur = node
    while cur.left:
        cur = cur.left
    return cur


def find_rightmost(node):
    cur = node
    while cur.right:
        cur = node.right
    return cur


def remove(root, key):
    if not root:
        return None

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        # Case #1. Tree consists only from one node
        if root.left is None and root.right is None:
            root = None

        # Case #2. Node has only one child
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
        # Case #3. Node has two child
        # We replace the value of the node and run it recursively
            p = find_leftmost(root.right)
            root.value = p.value
            root.right = remove(root.right, p.value)

    return root


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
    print("Success")


# test()
