# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ptr = head
        n = 0
        while ptr:
            n+=1
            ptr = ptr.next

        total_len, extra = divmod(n,k)

        ans = []
        cur = head
        for i in range(k):
            head = ptr = ListNode(None)
            for j in range(total_len+(i<extra)):
                ptr.next = ListNode(cur.val)
                ptr = ptr.next
                if cur:
                    cur = cur.next
            
            ans.append(head.next)
        return ans
        
