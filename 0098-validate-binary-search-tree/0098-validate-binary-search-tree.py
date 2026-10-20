# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def dfs(l, u, n):
            if not n:
                return True
            
            if n.val >= u or n.val <= l:
                return False

            return dfs(l, n.val, n.left) and dfs(n.val, u, n.right)

        return dfs(-float("inf"), float("inf"), root)    
            