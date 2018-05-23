class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def tilt(self, root):
        self.t = 0
        self.tree_sum(root)
        return self.t


    def tree_sum(self, node):
        if not node:
            return 0
        left = self.tree_sum(node.left)
        right = self.tree_sum(node.right)
        self.t += abs(left - right)
        return node.val + left + right

if __name__ == '__main__':
    #    1
    tree = TreeNode(1)

    #    1
    #  /   \
    # 2     3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    #      5
    #    /   \
    #   2     6
    #  / \     \
    # 1   3     8
    #          /
    #         7
    tree2 = TreeNode(5)
    tree2.left = TreeNode(2)
    tree2.left.left = TreeNode(1)
    tree2.left.right = TreeNode(3)
    tree2.right = TreeNode(6)
    tree2.right.right = TreeNode(8)
    tree2.right.left = TreeNode(7)

    assert(Solution().tilt(tree) == 0)
    assert(Solution().tilt(tree1) == 1)
    assert(Solution().tilt(tree2) == 18)
