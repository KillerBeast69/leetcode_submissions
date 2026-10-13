# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        dum = ListNode(0, head)
        pre = dum
        
        for _ in range(length - n):
            pre = pre.next

        pre.next = pre.next.next
        return dum.next
