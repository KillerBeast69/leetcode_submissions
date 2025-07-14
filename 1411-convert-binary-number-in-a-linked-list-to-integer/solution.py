# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bit = 1
        total = 0
        cur = head
        nodes = []
        while(cur):
            nodes.append(cur.val)
            cur = cur.next
        for i in nodes[::-1]:
            if i == 0:
                bit = bit * 2
            else:
                total = total + bit
                bit = bit * 2
        return total
