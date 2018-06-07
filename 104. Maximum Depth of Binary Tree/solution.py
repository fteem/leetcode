def max_depth(root):
    if not root:
        return 0

    left = 0
    right = 0

    if root.left:
        left = max_depth(root.left)
    if root.right:
        right = max_depth(root.right)
    return 1 + max(left, right)
