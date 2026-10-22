# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float('-inf')

        def dfs(node):
            nonlocal maxi
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val

            maxi = max(
                maxi,
                val,
                val + left,
                val + right,
                val + left + right,
            )

            return max(
                val,
                val + left,
                val + right,
            )

        dfs(root)
        return maxi