def split(root, k):
    if root is None:
        return None, None

    # print("\nNode", root.value)

    # ->. We want all the nodes from the left subtree,
    # plus some nodes from the right
    if root.left and root.left.size + 1 <= k:
        # print("->")
        k_fixed = k - (1 + root.left.size)
        root.right, right_side = split(root.right, k_fixed)
        # print("L, R", root.right, right_side)
        
        # Update size
        # print("Updating size, root", root.value)
        root.size -= right_side.size

        return root, right_side
    
    # <-. We want some nodes from the left tree
    # print("<-")
    left_side, root.left = split(root.left, k)

    if left_side is None:
        if k == 0:
            return None, root
        return root, None
    
    root.size -= left_side.size
    return left_side, root
