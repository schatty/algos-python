# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def recursive_collection(node, store):
    if node is None:
        return None

    l = recursive_collection(node.left, store)
    r = recursive_collection(node.right, store)
    split_max = []
    if l is not None: split_max.append(l)
    if r is not None: split_max.append(r)
    if len(split_max):
        split_max_val = max(split_max)
    else:
        split_max_val = -float('inf')

    if len(split_max):
        cur_node_max = max(node.value, *[x + node.value for x in split_max])
    else:
        cur_node_max = node.value
   
    if split_max_val > cur_node_max:
        store.append(split_max_val)

    if r and l:
        store.append(r + l + node.value)

    return cur_node_max


def solution(root) -> int:
    store = []
    val = recursive_collection(root, store)
 
    if len(store):
        return max(*store, val)
    return val
 

def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)

    assert solution(node5) == 6

def test2():
    node1 = Node(-1, None, None)
    assert solution(node1) == -1

def test3():
    node2 = Node(-2, None, None)
    node3 = Node(-3, None, None)
    node1 = Node(1, node2, node3)
    assert solution(node1) == 1

# test()
# test2()
# test3()
