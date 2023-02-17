# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self,ptr):
        if not ptr:
            return 
        self.traverse(ptr.left)
        if self.prev:
            self.min_diff = min(self.min_diff,ptr.val-self.prev.val)
        self.prev = ptr
        self.traverse(ptr.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = 1e6
        self.prev = None
        self.traverse(root)
        return self.min_diff
        
