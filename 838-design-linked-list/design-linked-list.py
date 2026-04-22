class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        for _ in range(index):
            if not temp:
                return -1
            temp= temp.next
        if not temp:
            return -1
        return temp.data

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        
    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        else:
            temp2 = self.head
            while temp2.next:
                temp2 = temp2.next
            temp2.next = temp
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index ==0:
            self.addAtHead(val)
            return
        temp = self.head
        for _ in range(index-1):
            if not temp:
                return
            temp = temp.next
        if temp:
            temp2=Node(val)
            temp2.next = temp.next
            temp.next = temp2

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index ==0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(index -1):
            if not temp.next:
                return
            temp = temp.next
        if not temp.next:
            return
        temp.next = temp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)