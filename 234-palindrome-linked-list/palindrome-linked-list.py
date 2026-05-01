# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s =f = head
        while f is not None:
            if f.next is None:
                s = s.next
                break
            s = s.next
            f =f.next.next
        prev = None
        curr = s
        while curr is not None:
            temp = curr.next
            curr.next = prev

            prev=curr
            curr = temp
        head2 = prev
        temp1, temp2 = head, head2
        while temp1 and temp2:
            if temp1.val != temp2.val:
                return False
            temp1,temp2 = temp1.next, temp2.next
        return True