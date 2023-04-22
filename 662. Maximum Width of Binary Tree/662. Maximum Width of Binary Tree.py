# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        prev_level,prev_num,max_width = 1,1,0

        queue = [(prev_level,prev_num,root)]
        while queue:
            level, num, node = queue.pop(0)

            if level>prev_level:
                prev_level = level
                prev_num = num

            max_width = max(max_width, num-prev_num+1)

            if node.left:
                queue.append((level+1,2*num,node.left))
            if node.right:
                queue.append((level+1,2*num+1,node.right))
        
        return max_width
