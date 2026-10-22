# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        
        def dfs(p, i):
            if not p or not i:
                return None
            
            r = TreeNode(p[0])
            m = i.index(p[0])
            r.left = dfs(p[1:m + 1], i[:m])
            r.right = dfs(p[m + 1:], i[m + 1:])

            return r

        return dfs(preorder, inorder)