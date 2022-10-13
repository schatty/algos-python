
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def Reverse(head: Node, left: int, right: int) -> Node:
    if right - left == 0:
        return head

    node = head
    cur, end_node = None, None
    prev_start = None
    for i in range(1, right + 1):
        if i == left:
            cur = node
        
        if i < left:
            prev_start = node

        if i == right:
            end_node = node
            break

        node = node.next
    
    end_next_node = None
    if end_node is not None:
        end_next_node = end_node.next

    if prev_start:
        prev_start.next = end_node
    else:
        head = end_node

    tmp = end_next_node
    tmp2 = cur.next

    while cur is not None and cur is not end_next_node:
        tmp2 = cur.next
        cur.next = tmp
        tmp = cur
        cur = tmp2

    return head




# n6 = Node(6)
# n5 = Node(5, n6)
# n4 = Node(4, n5)

# n3 = Node(3, None)
# n2 = Node(2, n3)
# n1 = Node(1, n2)

# def print_list(head):
#     node = head
#     while node is not None:
#         print(node.value, end=" ")
#         node = node.next
#         _ = input()
#     print()

# print("Before")
# print_list(n1)
# head = Reverse(n1, 1, 1)
# print("After")
# print_list(head)
