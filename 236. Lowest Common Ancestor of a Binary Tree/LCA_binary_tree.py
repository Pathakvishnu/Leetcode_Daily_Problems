"""
Lowest Common Ancestor of a Binary Search Tree
Smallest Common Region
Find Players With Zero or One Losses
Lowest Common Ancestor of a Binary Tree II
Lowest Common Ancestor of a Binary Tree III
Lowest Common Ancestor of a Binary Tree IV
Step-By-Step Directions From a Binary Tree Node to Another

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None,p,q):
            return root

        left,right = (self.lowestCommonAncestor(child,p,q) for child in (root.left,root.right))

        return root if left and right else left or right

