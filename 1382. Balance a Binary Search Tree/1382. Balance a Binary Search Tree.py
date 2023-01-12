# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrToBST(self,nums):
        n = len(nums)
        if not nums:
            return None
        mid = n//2
        return TreeNode(nums[mid],self.sortedArrToBST(nums[:mid]),
        self.sortedArrToBST(nums[mid+1:]))

    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_data = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_data.append(root.val)
            inorder(root.right)
        inorder(root)

        return self.sortedArrToBST(inorder_data)

    