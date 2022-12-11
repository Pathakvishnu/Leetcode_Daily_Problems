# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Definition for a binary tree node.
        if not root:
            return []
        paths = []
        def dfs(pt,pathSum,path):
            if not pt.left and not pt.right and pathSum==pt.val:
                paths.append(path+[pt.val])
                return 
            if pt.left:
                dfs(pt.left,pathSum-pt.val,path+[pt.val])
            if pt.right:
                dfs(pt.right,pathSum-pt.val,path+[pt.val])

        dfs(root,targetSum,[])
        # print(paths)
        return paths
