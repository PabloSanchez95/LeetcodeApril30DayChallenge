from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        res = self.helper(preorder, float("inf"))
        return res

    def helper(self, preorder, limit):
        if preorder and preorder[0] < limit:
            val = preorder.pop(0)
            node = TreeNode(val)
            node.left = self.helper(preorder, val)
            node.right = self.helper(preorder, limit)

            return node
        return None


if __name__ == "__main__":
    arr = [8, 5, 1, 7, 10, 12]
    res = Solution().bstFromPreorder(arr)
    print(res)
