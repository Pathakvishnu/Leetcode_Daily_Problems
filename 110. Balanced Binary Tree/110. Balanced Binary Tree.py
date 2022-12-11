# Definition for a binary tree node.
from argparse import OPTIONAL

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: OPTIONAL[TreeNode]) -> bool:
        # so height of binary tree is balanced if abs(left tree hgt - right tree ght) <=1
        if not root:
            return True
        def check(ptr):
            if not ptr:
                return 0
            left_hgt = check(ptr.left)
            rgt_hgt = check(ptr.right)
            
            if left_hgt==-1 or rgt_hgt==-1 or abs(left_hgt-rgt_hgt)>1:
                return -1
            return max(left_hgt,rgt_hgt) + 1

        if check(root)>0:
            return True
        return False