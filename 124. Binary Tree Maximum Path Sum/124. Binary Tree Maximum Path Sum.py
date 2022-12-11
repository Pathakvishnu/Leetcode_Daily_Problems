# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calculateSum(self,ptr):
        if not ptr:
            return 0
        ls = self.calculateSum(ptr.left)
        rs = self.calculateSum(ptr.right)

        # to ignore negative left and right sum
        if ls<0:
            ls=0
        if rs<0:
            rs=0

        self.max_path_sum = max(self.max_path_sum,ptr.val +ls+rs)
        return ptr.val + max(ls,rs)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum=-1e9
        self.calculateSum(root)
        return self.max_path_sum
        