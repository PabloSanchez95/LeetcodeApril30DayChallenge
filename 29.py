# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        self.max = float('-inf')
        self.get_sum(root)
        return self.max

    def get_sum(self, root):
        if root is None:
            return 0
        else:
            ls = max(self.get_sum(root.left), 0)
            rs = max(self.get_sum(root.right), 0)
            self.max = max(self.max, ls + rs + root.val)
            return max(ls, rs, 0) + root.val
