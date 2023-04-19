# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag = 0

        def dfs(node, prev_turn, zigzag_len):
            if node:
                self.max_zigzag = max(zigzag_len,self.max_zigzag)
                if prev_turn=='R':
                    dfs(node.left,'L',zigzag_len+1)
                    dfs(node.right,'R',1)

                if prev_turn=='L':
                    dfs(node.right,'R',zigzag_len+1)
                    dfs(node.left,'L',1)

        dfs(root,'L',0)
        dfs(root,'R',0)

        return self.max_zigzag

