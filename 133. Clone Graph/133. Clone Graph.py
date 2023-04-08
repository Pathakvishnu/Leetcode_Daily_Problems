"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        
        queue,cloneDict = [node],{node.val:Node(node.val,[])}

        while queue:
            curr = queue.pop(0)
            cur_clone = cloneDict[curr.val]

            for neigh in curr.neighbors:
                if neigh.val not in cloneDict:
                    queue.append(neigh)
                    cloneDict[neigh.val] = Node(neigh.val,[])

                cur_clone.neighbors.append(cloneDict[neigh.val])
        return cloneDict[node.val]
