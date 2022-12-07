# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self,ptr,low,high):
            if ptr is None:
                return 0
            
            if low<=ptr.val<=high:
                self.tot_sum+=ptr.val

            elif ptr.val<low:
                ptr.left = None
            
            elif ptr.val>high:
                ptr.right=None
                
            self.traverse(ptr.left,low,high)
            self.traverse(ptr.right,low,high)
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.tot_sum=0
        self.traverse(root,low,high)
        return self.tot_sum

             