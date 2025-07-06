class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        cur = self.head.next
        while(cur and index > 0):
            cur = cur.next
            index -= 1
        if index == 0 and cur != self.tail and cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode, next, prev = ListNode(val), self.head.next, self.head
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode, next, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while(cur and index > 0):
            cur = cur.next
            index -= 1
        if cur and index == 0:
            newNode, next, prev = ListNode(val), cur, cur.prev
            prev.next = newNode
            next.prev = newNode
            newNode.next = next
            newNode.prev = prev
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while(cur and index > 0):
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.tail:
            next, prev = cur.next, cur.prev
            prev.next = next
            next.prev = prev

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
