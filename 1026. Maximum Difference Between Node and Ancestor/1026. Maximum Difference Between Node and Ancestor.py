# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.max_diff = 0
        self.traverse(root, root.val, root.val)

        return self.max_diff

    def traverse(self,ptr,min_val,max_val):
        if not ptr: 
            return

        self.max_diff = max(self.max_diff, abs(ptr.val-min_val), abs(ptr.val-max_val))
        min_val, max_val = min(min_val, ptr.val), max(max_val, ptr.val)
        self.traverse(ptr.left, min_val, max_val)
        self.traverse(ptr.right, min_val, max_val)

        