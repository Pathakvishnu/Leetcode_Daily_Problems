# Definition for a binary tree node.
import heapq
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        def dfs(ptr):
            candi = [0]
            if not ptr:
                return 0
            for child in [ptr.left,ptr.right]:
                cur = dfs(child)
                if child and child.val==ptr.val:
                    candi.append(cur)

            candi = heapq.nlargest(2,candi)
            res[0] = max(res[0],sum(candi))
            return max(candi)+1

        dfs(root)
        return res[0]
