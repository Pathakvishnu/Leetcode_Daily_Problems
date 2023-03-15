# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        null_node = False
        while queue:
            node = queue.pop(0)
            if not node:
                null_node = True
            else:
                if null_node:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        
        return True
