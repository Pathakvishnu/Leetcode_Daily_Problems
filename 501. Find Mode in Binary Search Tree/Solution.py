# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, frequency):
            nonlocal max_freq
            if not node:
                return 

            frequency[node.val]+=1
            if max_freq<frequency[node.val]:
                max_freq = frequency[node.val]

            dfs(node.left,frequency)
            dfs(node.right,frequency)

            
        max_freq = 0
        frequency = defaultdict(int)
        dfs(root, frequency)

        ans = []
        for key in frequency:
            if frequency[key]==max_freq:
                ans.append(key)

        return ans
