def has_path_sum(root, sum):
    if not root:
        return False

    if not root.left and not root.right:
        if sum - root.val == 0:
            return True
        else:
            return False

    left = False
    right = False
    if root.left:
        has_path_sum(root.left, sum - root.val)
    if root.right:
        has_path_sum(root.right, sum - root.val)

    return left or right
