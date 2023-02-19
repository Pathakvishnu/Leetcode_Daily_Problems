from typing import Optional
from pyparsing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        level = 0
        # if level%2==0, we do l to r else r to l
        # it same as bfs, but for alternate level order of retirval of node will be different
        ans = list()
        while queue:
            res = []
            temp = []
            if not level%2:
                while queue:
                    node = queue.pop(0)
                    res.append(node.val)
                    for child in [node.left,node.right]:
                        if child:
                            temp.append(child)
                ans.append(res)


            if level%2:
                while queue:
                    node = queue.pop(0)
                    res.append(node.val)
                    for child in [node.left,node.right]:
                        if child:
                            temp.append(child)
                ans.append(res[::-1])
                
            queue = temp
            level+=1
        return ans
            