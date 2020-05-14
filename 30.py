# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        N = len(arr)

        def isLeaf(node):
            return node.left is None and node.right is None

        def visit(node, index):
            if node is None:
                return False
            if index == N - 1:
                return node.val == arr[index] and isLeaf(node)

            if node.val == arr[index]:
                return visit(node.left, index + 1) or visit(node.right, index + 1)
            return False

        return visit(root, 0)
