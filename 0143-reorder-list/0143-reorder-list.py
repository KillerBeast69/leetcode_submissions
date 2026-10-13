# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        j = s.next
        s.next = None
        pre = None

        while j:
            tmp = j.next
            j.next = pre
            pre = j
            j = tmp

        i, j = head, pre
        while i and j:
            tmp1, tmp2 = i.next, j.next
            i.next = j
            j.next = tmp1
            i, j = tmp1, tmp2
        