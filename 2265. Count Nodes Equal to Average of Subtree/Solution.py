# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node:
            return 0,0 # sum,cnt

        left_tree_sum, left_tree_cnt = self.dfs(node.left)
        rgt_tree_sum, rgt_tree_cnt = self.dfs(node.right)

        node_sum = left_tree_sum + rgt_tree_sum + node.val
        node_cnt = left_tree_cnt + rgt_tree_cnt + 1

        if node_sum//node_cnt == node.val:
            self.match+=1
        
        return node_sum, node_cnt

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:        
        self.match = 0
        self.dfs(root)
        return self.match

            

        
