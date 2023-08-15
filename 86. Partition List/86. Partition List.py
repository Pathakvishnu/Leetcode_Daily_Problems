# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = smaller_than_x = ListNode(0)
        large = larger_than_x = ListNode(0)

        while head:
            if head.val<x:
                small.next = head
                small = small.next

            else:
                large.next = head
                large = large.next

            head = head.next
        
        large.next = None
        small.next = larger_than_x.next

        return smaller_than_x.next

head = [1,4,3,2,5,2]
x = 3
