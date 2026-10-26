class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head

        for _ in range(index):
            cur = cur.next
        cur =cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        next = self.head.next
        prev = self.head
        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.tail
        prev = self.tail.prev
        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur = cur.next
        node = ListNode(val)
        next = cur
        prev = cur.prev

        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur = cur.next
        
        if cur and cur != self.tail:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

        self.size -= 1