class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) # dummy node
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head.next
        for i in range(index):
            cur = cur.next
        
        return cur.val


    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        cur = self.head
        node.next = cur.next
        cur.next = node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        node = ListNode(val)
        while cur.next:
            cur = cur.next
        cur.next = node
        self.size +=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        cur = self.head
        node = ListNode(val)
        for i in range(index):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.size +=1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -=1

