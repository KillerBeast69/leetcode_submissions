# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        big = -inf
        while slow:
            top = stack.pop()
            total = slow.val + top
            big = max(big, total)
            slow = slow.next
        return big

