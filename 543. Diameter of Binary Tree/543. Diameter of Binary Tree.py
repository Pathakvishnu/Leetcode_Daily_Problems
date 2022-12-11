# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self,ptr):
            if not ptr:
                return 0
            left_hgt = self.check(ptr.left)
            rgt_hgt = self.check(ptr.right)
            self.max_width = max(self.max_width,left_hgt+rgt_hgt)

            return max(left_hgt,rgt_hgt) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Definition for a binary tree node.
        if not root:
            return True

        self.max_width = 0
    
        self.check(root)
        return self.max_width