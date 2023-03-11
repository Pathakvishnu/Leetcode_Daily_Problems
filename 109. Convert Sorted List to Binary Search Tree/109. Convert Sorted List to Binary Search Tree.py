# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head

        def count_len(ptr):
            count=0
            while ptr:
                count+=1
                ptr=ptr.next
            return count

        def create_bst(left,right):
            nonlocal head
            if left>right: 
                return None
            mid = left+(right-left)//2
            left_node = create_bst(left,mid-1)
            root = TreeNode(head.val)
            head = head.next

            root.left = left_node
            root.right = create_bst(mid+1,right)

            return root
        return create_bst(0,count_len(head)-1)