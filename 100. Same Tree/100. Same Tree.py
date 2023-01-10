# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val!=q.val:
            return False
        
        if not self.isSameTree(p.left,q.left):
            return False
        if not self.isSameTree(p.right,q.right):
            return False

        return True        
