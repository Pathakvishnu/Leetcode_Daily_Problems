from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodesBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_count = 1
        queue = [root.left,root.right]

        while queue:
            ptr = queue.pop()
            if ptr:
                node_count+=1
                if ptr.left:
                    queue.append(ptr.left)
                if ptr.right:
                    queue.append(ptr.right)
        
        return node_count

    def countNodesDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftNodes = self.countNodesDFS(root.left)
        rightNodes = self.countNodesDFS(root.right)

root = [1,2,3,4,5,6]
