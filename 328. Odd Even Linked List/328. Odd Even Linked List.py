# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        odd = head
        even = head.next
        even_start = even

        while even!=None and even.next!=None:
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = even_start
            odd = odd.next
            even = even.next

        return head
            
