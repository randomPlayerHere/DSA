# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kth_node(head,k):
            if head is None:
                return 0
            temp = head
            for _ in range(k-1):
                temp =temp.next
                if temp is None:
                    return 0
            return temp
        
        def reverse_ll(head):
            prev = None
            curr = head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        sub_head, sub_end = head, kth_node(head,k)
        prev_sub_end = None
        new_head = None
        while sub_end:
            sub_next_head = sub_end.next
            sub_end.next = None
            reverse_head = reverse_ll(sub_head)
            if sub_head ==head:
                new_head = reverse_head
            else:
                prev_sub_end.next = reverse_head
            prev_sub_end = sub_head
            sub_head = sub_next_head
            sub_end = kth_node(sub_head,k)
        prev_sub_end.next = sub_head
        return new_head
