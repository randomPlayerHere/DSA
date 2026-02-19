import math 
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        middle = count // 2
        temp = head
        for _ in range(middle - 1):
            temp = temp.next
        temp.next = temp.next.next
        
        return head
