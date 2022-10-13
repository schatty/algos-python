"""
https://contest.yandex.ru/contest/24810/run-report/69580368/

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

* O(h) - finding element, where h is the height of the tree
* O(h) - recursive deletion of the node in the worst case.

T = O(h) + O(h) = O(h)

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

    # Check if key was found
    if d is None:
        return None

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
