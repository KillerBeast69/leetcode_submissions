# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dum = ListNode()
        cur = dum
        n1, n2 = list1, list2
        while n1 and n2:
            if n1.val <= n2.val:
                cur.next = n1
                n1 = n1.next
                cur = cur.next
            else:
                cur.next = n2
                n2 = n2.next
                cur = cur.next
            
        if n1:
            cur.next = n1
        elif n2:
            cur.next = n2

        return dum.next