# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product=total = 0
        def dfs(ptr,sumProduct=False):
            if not ptr:
                return 0
            left_sum = dfs(ptr.left,True)
            rgt_sum = dfs(ptr.right,True)
            if sumProduct:
                self.max_product = max(self.max_product,
                                    left_sum*(total-left_sum),
                                    rgt_sum*(total-rgt_sum))
    
            return left_sum + rgt_sum + ptr.val

        total = dfs(root)
        dfs(root,True)

        return self.max_product%(10**9+7)
