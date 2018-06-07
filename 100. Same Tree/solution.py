def is_same_tree(p, q):
    if p == q:
        return True
    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
