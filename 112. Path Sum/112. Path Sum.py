# Definition for a binary tree node.
from argparse import OPTIONAL


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: OPTIONAL[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        def dfs(pt,pathSum):
            if not pt.left and not pt.right and pathSum==pt.val:
                return True
            left=False
            right=False
            if pt.left:
                left =  dfs(pt.left,pathSum-pt.val)
            if pt.right:
                right =  dfs(pt.right,pathSum-pt.val)

            return left or right
        return dfs(root,targetSum)
