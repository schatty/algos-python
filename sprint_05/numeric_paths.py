class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def walk(node, cur_path, store):
    if node is None:
        return
    if node.left is None:
        if node.right is None:
            store.append(cur_path + str(node.value))
            return

    walk(node.left, cur_path + str(node.value), store)
    walk(node.right, cur_path + str(node.value), store)


def solution(root) -> int:
    store = []
    walk(root, "", store)
    return sum(map(int, store))


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)
    
    assert solution(node5) == 275

# test()
