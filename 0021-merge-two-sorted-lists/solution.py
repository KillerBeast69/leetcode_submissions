# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = list1
        a2 = list2
        dummy = ListNode()
        tail = dummy
        while(a1 and a2):
            if a1.val < a2.val:
                tail.next = a1
                a1 = a1.next 
            else:
                tail.next = a2
                a2 = a2.next
            tail = tail.next
        if a1:
            tail.next = a1
        elif a2:
            tail.next = a2
        return dummy.next

