# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # we will travel both tree simultaneously
        # while traversing if both node is not null add them
        # if one of the node is not null keep that node value
        # if both node is null keep null

        if not root1 and not root2: return None
        merged = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        merged.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        merged.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
        return merged