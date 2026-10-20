# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(n):
            if p.val < n.val and q.val < n.val:
                return dfs(n.left)
            
            if p.val > n.val and q.val > n.val:
                return dfs(n.right)
            
            return n
            
        return dfs(root)