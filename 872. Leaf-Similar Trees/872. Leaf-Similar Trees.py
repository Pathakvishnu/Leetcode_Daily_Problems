# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        def traverse(ptr,val=[]):
            if not ptr:
                return None 
            if not ptr.left and not ptr.right:
                val.append(ptr.val)
            traverse(ptr.left,val)
            traverse(ptr.right,val)
            return val
        
        a = traverse(root1,[])
        b = traverse(root2,[])
        
        if len(a)!=len(b):
            return False

        for i,j in zip(a,b):
            if i!=j:
                return False
           
        return True
