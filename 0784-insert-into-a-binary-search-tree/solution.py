# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        condition = True
        if not root:
            return TreeNode(val)
        while(condition == True):
            if val > cur.val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    condition = False
                else:
                    cur = cur.right
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    condition = False
                else:
                    cur = cur.left
        return root
