"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        nhead = Node(head.val)
        head_temp = head.next
        nhead_temp = nhead
        head.son = nhead
        while head_temp is not None:
            temp = Node(head_temp.val)
            nhead_temp.next = temp
            nhead_temp = nhead_temp.next
            head_temp.son = nhead_temp
            head_temp = head_temp.next
        nhtemp,htemp = nhead, head
        while htemp is not None:
            if htemp.random ==None:
                nhtemp.random = None
            else:
                nhtemp.random = htemp.random.son
            nhtemp = nhtemp.next
            htemp = htemp.next
        return nhead

        