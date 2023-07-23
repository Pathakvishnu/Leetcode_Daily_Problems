# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # full binary tree with even nodes is not possible
        if not n%2:
            return []
        if n==1:
            return [TreeNode()]
        
        ans = []

        for num_nodes in range(1,n,2):
            left = self.allPossibleFBT(num_nodes)
            right = self.allPossibleFBT(n-num_nodes-1)

            for l in left:
                for r in right:
                    tree = TreeNode(0,l,r)
                    ans.append(tree)

        return ans

n = 7
obj = Solution()
obj.allPossibleFBT(n)
