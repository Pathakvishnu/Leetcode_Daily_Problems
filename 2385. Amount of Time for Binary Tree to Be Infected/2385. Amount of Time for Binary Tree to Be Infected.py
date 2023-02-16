from collections import defaultdict
from pyparsing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int: 
        # covert to undirecred graph
        stack = [root]
        graph = defaultdict(list)
        while stack:
            ptr = stack.pop()
            for child in [ptr.left,ptr.right]:
                if not child:
                    continue
                graph[ptr.val].append(child.val)
                graph[child.val].append(ptr.val)
                stack.append(child)

        # at t=0, start is infected 
        # at t=1, start's one hop neighbours will get infected

        infected = [(start,0)] # node,time
        visited = set()
        max_t = 0
        while infected:
            node,t = infected.pop()
            max_t = max(max_t,t)
            visited.add(node)
            for neg in graph[node]:
                if neg in visited:
                    continue
                infected.append((neg,t+1))

        return max_t
        
root = [1,5,3,None,4,10,6,9,2]
start = 3
        
                
        