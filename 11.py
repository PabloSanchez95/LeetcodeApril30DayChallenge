# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.final_value = 1

    def depth(self, node):
        if not node:
            return 0
        left_value = self.depth(node.left)
        right_value = self.depth(node.right)
        max_value = left_value + right_value + 1
        self.final_value = max(max_value, self.final_value)
        return max(left_value, right_value) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.depth(root)
        return self.final_value - 1


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(tree1))
