# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointer approach
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        return slow

head = [1,2,3,4,5]
