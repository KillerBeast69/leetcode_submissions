# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque([])
        q.append(root)
        res = []
        while q:
            level = []
            for i in range(len(q)):
                c = q.popleft()
                level.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)

            res.append(level)

        return res