# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_A = []
        stack_B = []

        ptr = l1
        while ptr:
            stack_A.append(ptr.val)
            ptr = ptr.next

        ptr = l2
        while ptr:
            stack_B.append(ptr.val)
            ptr = ptr.next

        del(ptr)

        ptr = ListNode()
        head = ptr
        res = []
        carry = 0
        while len(stack_A) or len(stack_B):
            ele_sum = 0
            ele_A = stack_A.pop() if len(stack_A)>0 else 0
            ele_B = stack_B.pop() if len(stack_B)>0 else 0
            ele_sum = ( ele_A+ele_B+carry)%10 if carry>0 else (ele_A + ele_B)%10
            carry = (ele_A + ele_B + carry)//10

            res.append(ele_sum)

        if carry>0:
            res.append(carry)
        
        for ele in res[::-1]:
            head.next = ListNode(ele)
            head = head.next

        return ptr.next




        
