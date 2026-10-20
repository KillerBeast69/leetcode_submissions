# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        cur = root
        q = deque([])
        q.append(cur)
        
        def dfs(n1, n2):
            if (n1 and not n2) or (n2 and not n1):
                return False

            if not n1 and not n2:
                return True

            if n1.val != n2.val:
                return False
            
            return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)

        while q:
            for i in range(len(q)):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                
                if dfs(c, subRoot):
                    return True
                
                continue
        
        return False