class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:

    def __init__(self):
        self.cur = None
        self.tail = None

    def push(self, x: int) -> None:
        newNode = ListNode(x)
        newNode.prev = self.cur
        self.cur = newNode
        self.tail = newNode

    def pop(self) -> int:
        value = self.tail.val
        if self.tail.prev == None:
            self.tail = None
            return value
        self.cur = self.tail.prev
        self.tail.prev.next = None
        self.tail.prev = None
        self.tail = self.cur
        return value

    def top(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        if self.tail == None:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
