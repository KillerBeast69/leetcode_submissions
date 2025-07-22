# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head.next
        behind = head
        while(behind.next):
            if cur.val == behind.val:
                behind.next = cur.next
                cur = cur.next
            else:
                behind = cur
                cur = cur.next
        return head
