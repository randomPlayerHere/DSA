# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =tail= ListNode(-1)
        carry = 0
        while l1 or l2:
            sum_here = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_here//10
            temp = ListNode(sum_here%10)
            tail.next = temp
            tail=tail.next
            l1 = (l1.next if l1 else None)
            l2=(l2.next if l2 else None)


        if carry:
            temp = ListNode(carry)
            tail.next = temp
        return dummy.next
