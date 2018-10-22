# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        def _check_height(node):
            if node is None:
                return 0
            left = _check_height(node.left)
            right = _check_height(node.right)
            if abs(left - right) <= 1:
                return max(left, right) + 1
            return 0

        return bool(_check_height(root))

if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    assert Solution().isBalanced(tree)

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.left.left.left = TreeNode(6)
    tree.left.left.right = TreeNode(7)
    assert Solution().isBalanced(tree) is False
