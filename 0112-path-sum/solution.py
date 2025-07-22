# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        path = []
        return self.way(root, total, targetSum)
    def way(self, root, total, targetSum):
        if not root:
            print("total: ", total)
            print(1)
            return False
        print("total before add: ", total)
        print(0)
        total = total + root.val
        print("total after add: ", total)
        if not root.left and not root.right and total == targetSum:
            print("total: ", total)
            print(3)
            return True

        if self.way(root.left, total, targetSum):
            print("total: ", total)
            print(4)
            return True
        if self.way(root.right, total, targetSum):
            print("total: ", total)
            print(5)
            return True
        print("total: ", total)
        print(6)
        return False
